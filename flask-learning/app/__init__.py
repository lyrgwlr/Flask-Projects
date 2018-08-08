from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)#实例化Flask核心对象
    
    #读取配置文件
    app.config.from_object('app.secure_config')
    app.config.from_object('app.setting_config')
    
    register_blueprint(app) #蓝图注册
    
    #数据库的初始化
    db.init_app(app)
    
    #loginManger的初始化
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web) #注册web蓝图
    