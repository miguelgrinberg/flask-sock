import eventlet
eventlet.monkey_patch()

from eventlet import wsgi
from flask import Flask, render_template
from flask_sock import Sock
app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        if data == 'close':
            break
        ws.send(data)


if __name__ == '__main__':
    wsgi.server(eventlet.listen(('', 5000)), app)
