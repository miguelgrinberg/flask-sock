from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(sock):
    while sock.connected:
        data = sock.receive()
        if data:
            sock.send(data)
