from app import create_app
from flask import render_template,url_for

app = create_app()

@app.route('/')
def index():
    return(render_template('base.html'))
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=app.config['DEBUG'])