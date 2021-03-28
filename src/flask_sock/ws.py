import threading
from wsproto import ConnectionType, WSConnection
from wsproto.events import (
    AcceptConnection,
    CloseConnection,
    Message,
    Request,
    Ping,
    TextMessage,
    BytesMessage,
)
from wsproto.frame_protocol import CloseReason


class ConnectionClosed(RuntimeError):
    pass


class WebSocket:
    def __init__(self, environ, receive_bytes=4096):
        self.receive_bytes = receive_bytes
        self.input_buffer = []
        self.event = threading.Event()
        self.connected = False

        self.stream = environ.get('werkzeug.socket')
        if self.stream is None:
            self.stream = environ.get('gunicorn.socket')
        if self.stream is None:
            raise RuntimeError('socket not available in WSGI environment')
        self.ws = WSConnection(ConnectionType.SERVER)

        in_data = b'GET / HTTP/1.1\r\n'
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                header = '-'.join([p.capitalize() for p in key[5:].split('_')])
                in_data += f'{header}: {value}\r\n'.encode()
        in_data += b'\r\n'
        self.ws.receive_data(in_data)

        self.thread = threading.Thread(target=self._thread)
        self.thread.start()
        self.event.wait()
        self.event.clear()

    def send(self, data):
        if not self.connected:
            raise ConnectionClosed()
        if isinstance(data, bytes):
            out_data = self.ws.send(Message(data=data))
        else:
            out_data = self.ws.send(TextMessage(data=str(data)))
        self.stream.send(out_data)

    def receive(self, timeout=None):
        while self.connected and not self.input_buffer:
            if not self.event.wait(timeout=timeout):
                return None
            self.event.clear()
        if not self.connected:
            raise ConnectionClosed()
        return self.input_buffer.pop(0)

    def close(self, reason=None, message=None):
        out_data = self.ws.send(CloseConnection(
            reason or CloseReason.NORMAL_CLOSURE, message))
        self.stream.send(out_data)

    def _thread(self):
        if not self._handle_events():
            return

        self.connected = True
        self.event.set()
        while self.connected:
            try:
                in_data = self.stream.recv(self.receive_bytes)
            except ConnectionResetError:
                self.connected = False
                break
            self.ws.receive_data(in_data)
            self.connected = self._handle_events()

    def _handle_events(self):
        keep_going = True
        out_data = b''
        for event in self.ws.events():
            if isinstance(event, Request):
                out_data += self.ws.send(AcceptConnection())
            elif isinstance(event, CloseConnection):
                out_data += self.ws.send(event.response())
                self.event.set()
                keep_going = False
            elif isinstance(event, Ping):
                out_data += self.ws.send(event.response())
            elif isinstance(event, TextMessage):
                self.input_buffer.append(event.data)
                self.event.set()
            elif isinstance(event, BytesMessage):
                self.input_buffer.append(event.data)
                self.event.set()
        if out_data:
            self.stream.send(out_data)
        return keep_going
