# flask-sock
WebSocket support for Flask (and possibly other WSGI frameworks). What makes
this package different than other WebSocket servers is that it does not require
a greenlet based server (gevent, eventlet) to work.

This WebSocket implementation is compatible with the following synchronous
web servers:

- Werkzeug (Flask's development web server)
- Gunicorn with the `gthread` worker

In addition to the servers above, the following asynchronous web servers are
supported when the Python standard library is monkey patched:

- Eventlet's WSGI server
- Gevent's WSGI server
- Gunicorn with the `eventlet` worker
- Gunicorn with the `gevent` worker

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
server.

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

### Running with eventlet

To serve your application with the eventlet WSGI server you can use the
following script:

```python
import eventlet
eventlet.monkey_patch()

from eventlet import wsgi
from module import app

wsgi.server(eventlet.listen(('', 5000)), app)
```

It is also possible to use Gunicorn's `eventlet` worker:

```bash
gunicorn -b :5000 --worker-class eventlet module:app
```

Gunicorn's `eventlet` worker handles a maximum of 1000 concurrent requests in a
single worker process by default. The maximum number of concurrent requests
can be changed with the `--worker-connections` option. The number of workers
can be changed with the `--workers` option.

### Running with gevent

To serve your application with the gevent WSGI server you can use the following
script:

```python
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from module import app

WSGIServer(('127.0.0.1', 5000), app).serve_forever()
```

It is also possible to use Gunicorn's `gevent` worker:

```bash
gunicorn -b :5000 --worker-class gevent module:app
```

Gunicorn's `gevent` worker handles a maximum of 1000 concurrent requests in a
single worker process by default. The maximum number of concurrent requests
can be changed with the `--worker-connections` option. The number of workers
can be changed with the `--workers` option.
