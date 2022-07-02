from flask import Flask


def create_app():
    app = Flask(__name__)

    # import blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # import WebSocket route
    from .ws import sock
    sock.init_app(app)

    return app
