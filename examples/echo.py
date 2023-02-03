from flask import Flask, render_template
from flask_sock import Sock
import json
import time, datetime
import threading

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')

def send_time(ws):
    # simple loop spiting server time into the ws chanel as a json structure
    while True:
        time.sleep(1)
        ws.send(json.dumps({"type": "clock", "text": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}))

@sock.route('/echo')
def echo(ws):
    # start a thread to activate the clock
    t = threading.Thread(target=send_time,args=(ws,))
    t.start()
    while True:
        data = ws.receive()
        if data == 'close':
            break
        # note that the data is now (from original code) an object to provide the type selector
        ws.send(json.dumps({"type": "log", "text": data}))


if __name__ == '__main__':
    app.run()
