from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config or {})
    return app

