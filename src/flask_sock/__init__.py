from functools import wraps
from flask import Blueprint, request, abort
from .ws import WebSocket, ConnectionClosed


class Sock:
    def __init__(self, app=None):
        self.app = None
        self.bp = None
        if app is None:
            self.bp = Blueprint('__flask_sock', __name__)
        else:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        if self.app is None:
            app.register_blueprint(self.bp)

    def route(self, path, **kwargs):
        def decorator(f):
            @wraps(f)
            def websocket_route(*args, **kwargs):
                try:
                    f(WebSocket(request.environ), *args, **kwargs)
                except ConnectionClosed:
                    pass
                return ''

            kwargs['websocket'] = True
            return (self.app or self.bp).route(path, **kwargs)(websocket_route)

        return decorator
