from flask import Flask, render_template
from flask_sock import Sock
import json
import time, datetime
import threading

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)

client_list = []


@app.route('/')
def index():
    return render_template('clock.html')


def send_time():
    while True:
        time.sleep(1)
        clients = client_list.copy()
        for client in clients:
            try:
                client.send(json.dumps({
                    'text': datetime.datetime.now().strftime(
                        '%Y-%m-%d %H:%M:%S')
                }))
            except:
                client_list.remove(client)


@sock.route('/clock')
def clock(ws):
    client_list.append(ws)
    while True:
        data = ws.receive()
        if data == 'stop':
            break
    client_list.remove(ws)


if __name__ == '__main__':
    t = threading.Thread(target=send_time)
    t.daemon = True
    t.start()
    app.run()
