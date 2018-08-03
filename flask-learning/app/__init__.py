from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)#实例化Flask核心对象
    
    #读取配置文件
    app.config.from_object('app.secure_config')
    app.config.from_object('app.setting_config')
    
    register_blueprint(app) #蓝图注册
    
    #数据库的初始化
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web) #注册web蓝图
    