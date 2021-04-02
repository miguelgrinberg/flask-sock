# flask-sock
WebSocket support for Flask (and possibly other WSGI frameworks). What makes
this package different than other WebSocket servers is that it does not require
a greenlet based server (gevent, eventlet) to work. This server is compatible
with Werkzeug (Flask's development web server) and Gunicorn.

## Installation

```bash
pip install flask-sock
```

## Example

```python
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)
```

## Running

To run an application that uses this package, you need to use a supported web
server.  At this time the supported servers are:

- Werkzeug (Flask development server)
- Gunicorn

### Running with Werkzeug

Werkzeug supports WebSocket routing in version 2, which at this time hasn't
been officially released. You can install a supported release candidate with
the following command:

```bash
pip install "werkzeug>=2.0.0rc3"
```

To run your application use the normal method that you always use. Both the
`flask run` and `app.run()` methods of starting the Flask application should
work.

### Running with Gunicorn

To use this package with Gunicorn you need to keep in mind that each active
WebSocket client will use up a worker. The most practical way to run a
WebSocket server is to use the `--threads` option to allocate the number of
clients that you need:

```bash
gunicorn -b :5000 --threads 100 module:app
```

It is also okay to use multiple workers, each with a number of allocated
threads:

```bash
gunicorn -b :5000 --workers 4 --threads 100 module:app
```
