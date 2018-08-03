from app import create_app

app = create_app()  #核心对象的新建与初始化

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])#运行服务器