from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@sock.route('/echo')
def echo(sock):
    while sock.connected:
        data = sock.receive()
        if data:
            sock.send(data)
