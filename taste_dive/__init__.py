from flask import Flask
from .main.routes import main
from .user.routes import user
from .extensions import db, bcrypt, login_manager


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("taste_dive.config.DevelopmentConfig")
    register_extensions(app)
    register_blueprint(app)
    return app


def register_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


def register_blueprint(app):
    app.register_blueprint(main)
    app.register_blueprint(user)
