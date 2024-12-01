# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Регистрируем Blueprint с маршрутами
    from .routes import bp
    app.register_blueprint(bp)

    return app
