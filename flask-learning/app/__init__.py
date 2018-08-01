from flask import Flask
from app.models.book import db
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure_config')
    app.config.from_object('app.setting_config')
    register_blueprint(app)
    db.init_app(app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)