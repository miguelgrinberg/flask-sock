# flask-sock
[![Build status](https://github.com/miguelgrinberg/flask-sock/workflows/build/badge.svg)](https://github.com/miguelgrinberg/flask-sock/actions) [![codecov](https://codecov.io/gh/miguelgrinberg/flask-sock/branch/main/graph/badge.svg)](https://codecov.io/gh/miguelgrinberg/flask-sock)

WebSocket support for Flask. What makes this extension different than others
is that it does not require a greenlet based server (gevent, eventlet) to work.

This WebSocket implementation is compatible with the Flask development web
server. For a production deployment it can be used with Gunicorn, Eventlet or
Gevent.

## Resources

- [Documentation](http://flask-sock.readthedocs.io/en/latest/)
- [PyPI](https://pypi.python.org/pypi/flask-sock)
- [Change Log](https://github.com/miguelgrinberg/flask-sock/blob/main/CHANGES.md)
