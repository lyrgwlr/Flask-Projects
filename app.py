# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,request,render_template,redirect,url_for,session,escape

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/hello')
#@app.route('/hello/<name>')
def hello():
    if 'username' in session:
        return render_template('hello.html',name='Login Successful,'+escape(session['username']),submitBtn = 'logout')
    else:
        return render_template('hello.html',name='You are not logged in!',submitBtn = 'back')

#@app.route('/user/<username>')
#def show_user_profile(username):
#    return 'User %s' % username
#
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    return 'Post %d' % post_id

#@app.route('/login',methods=['GET','POST'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if request.form['username']=='admin' and request.form['password']=='admin':
#            return redirect(url_for('hello',name=request.form['username']))
#        else:
#            error = 'Invalid username/password'
#    return render_template('login.html',error=error)
      
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != '':
            session['username'] = request.form['username']
        return redirect(url_for('hello'))
    return render_template('login.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
    if request.method == 'POST':
        print(dict(request.form))
        if 'logout' in dict(request.form).keys():
            session.pop('username',None)
            return redirect(url_for('index'))
        if 'back' in dict(request.form).keys():
            return redirect(url_for('index'))
    return redirect(url_for('hello'))
if __name__ == '__main__':
    app.run(debug=True)