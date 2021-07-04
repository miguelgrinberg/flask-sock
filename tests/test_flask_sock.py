import unittest
from flask import Flask

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

        sock.init_app(app)

        assert sock.app is None
        assert sock.bp is not None
        assert app.url_map._rules[0].rule == '/ws'
        assert app.url_map._rules[0].websocket is True
