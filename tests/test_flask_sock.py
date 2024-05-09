import unittest
from unittest import mock

from flask import Flask, Blueprint

import flask_sock


class FlaskSockTestCase(unittest.TestCase):
    def test_create_direct(self):
        app = Flask(__name__, static_folder=None)
        sock = flask_sock.Sock(app)

        @sock.route('/ws')
        def ws(ws):
            pass

        assert sock.app == app
        assert sock.bp is None
        assert app.url_map._rules[0].rule == '/ws'
        assert app.url_map._rules[0].websocket is True

    def test_create_indirect(self):
        app = Flask(__name__, static_folder=None)
        sock = flask_sock.Sock()

        @sock.route('/ws')
        def ws(ws):
            pass

        assert sock.app is None
        assert sock.bp is not None

        sock.init_app(app)

        assert sock.app is not None
        assert sock.bp is not None
        assert app.url_map._rules[0].rule == '/ws'
        assert app.url_map._rules[0].websocket is True

    def test_create_blueprint(self):
        app = Flask(__name__, static_folder=None)
        bp = Blueprint('bp', __name__)

        sock = flask_sock.Sock()

        @sock.route('/ws', bp=bp)
        def ws(ws):
            pass

        assert sock.app is None
        assert sock.bp is None

        sock.init_app(app)
        app.register_blueprint(bp, url_prefix='/bp')

        assert sock.app is not None
        assert sock.bp is None

        @sock.route('/ws')
        def ws2(ws):
            pass

        assert app.url_map._rules[0].rule == '/bp/ws'
        assert app.url_map._rules[0].websocket is True
        assert app.url_map._rules[1].rule == '/ws'
        assert app.url_map._rules[1].websocket is True

    def test_decorator_wraps_properly(self):
        app = Flask(__name__, static_folder=None)
        sock = flask_sock.Sock(app)
        route = sock.route('/ws')

        def ws_func(ws):
            pass

        routed_ws_func = route(ws_func)

        assert routed_ws_func.__wrapped__ is ws_func
        assert routed_ws_func.__name__ == ws_func.__name__
        assert routed_ws_func.__doc__ == ws_func.__doc__
        assert app.url_map._rules[0].endpoint == 'ws_func'
        assert app.view_functions['ws_func'] is routed_ws_func

    def test_stacked_routes(self):
        app = Flask(__name__, static_folder=None)
        sock = flask_sock.Sock(app)

        @sock.route('/ws')
        @sock.route('/ws/<optional>')
        def ws_func(ws, optional=None):
            pass

        assert app.url_map._rules[0].rule == '/ws/<optional>'
        assert app.url_map._rules[0].endpoint == 'ws_func'
        assert app.url_map._rules[1].rule == '/ws'
        assert app.url_map._rules[1].endpoint == 'ws_func'

    def test_client_request(self):
        app = Flask(__name__, static_folder=None)
        sock = flask_sock.Sock(app)
        mock_ws = mock.Mock()
        client = app.test_client()

        def fake_simple_websocket_server(environ, **options):
            mock_ws.mode = 'werkzeug'
            return mock_ws

        @sock.route('/ws/test')
        def ws_func(ws):
            assert ws is mock_ws
            ws.test()

        with mock.patch('flask_sock.Server', fake_simple_websocket_server):
            assert mock_ws.mock_calls == []

            client.open(method='GET', url_scheme='ws', path='/ws/test')

            assert mock_ws.mock_calls == [mock.call.test(), mock.call.close()]
