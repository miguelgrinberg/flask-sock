Installation
------------

::

    pip install flask-sock

Configuration
-------------

The only configuration option is ``SOCK_SERVER_OPTIONS``. If this option is
present in the application instance's ``config`` object, it must be a
dictionary with configuration options for the WebSocket server. Notable
options include:

- ``ping_interval``: Send ping packets to clients at the requested interval in
  seconds. Set to ``None`` (the default) to disable ping/pong logic. Enable to
  prevent disconnections when the line is idle for a certain amount of time, or
  to detect unresponsive clients and disconnect them. A recommended interval is
  25 seconds.
- ``max_message_size``: The maximum size allowed for a message, in bytes, or
  ``None`` for no limit. The default is ``None``.

Example::

    app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

The complete list of available options is documented in the constructor of the
`simple_websocket.Server <https://simple-websocket.readthedocs.io/en/latest/api.html#the-server-class>`_
class.

Example
-------

::

    from flask import Flask
    from flask_sock import Sock

    app = Flask(__name__)
    sock = Sock(app)


    @sock.route('/echo')
    def echo(ws):
        while True:
            data = ws.receive()
            ws.send(data)
