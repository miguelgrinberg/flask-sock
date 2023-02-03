from flask import Flask, render_template
from flask_sock import Sock
import json
import time, datetime
import threading

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)

listners = {}


@app.route('/')
def index():
    return render_template('index_clock.html')

def send_time():
    while True:
        time.sleep(1)
        keys = list(listners.keys())
        for key in keys:
            try:
                listners[key].send(json.dumps({"type": "clock", "text": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}))
            except:
                del listners[key]

@sock.route('/echo')
def echo(ws):
    key = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    listners[key] = ws
    while True:
        data = ws.receive()
        if data == 'close':
            break
        ws.send(json.dumps({"type": "log", "text": data}))

t = threading.Thread(target=send_time,args=())
t.start()

if __name__ == '__main__':
    app.run()
