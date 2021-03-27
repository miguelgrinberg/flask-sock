# flask-sock
WebSocket support for Flask

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
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)
```
