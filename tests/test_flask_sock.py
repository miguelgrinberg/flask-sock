import unittest
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
