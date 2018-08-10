from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure_config')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.real import real
    app.register_blueprint(real)
    from app.handler import handler
    app.register_blueprint(handler)