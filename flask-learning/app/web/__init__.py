from flask import Blueprint 

web = Blueprint('web',__name__)#实例化蓝图，'web'是蓝图的名字

from app.web import book