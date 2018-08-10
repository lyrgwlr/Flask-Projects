from . import real
from flask import render_template,url_for,request
import requests

base_url = 'http://116.62.151.23/?type='

@real.route('/base')
def base():
    return(render_template('realbase.html'))
    
@real.route('/redray/<room>')
def redray(room):
    redray_url = base_url + 'send_sensor&info=' + room + '2'
    requests.get(redray_url)
    return(render_template('realsuccess.html'))

@real.route('/fall/<int:person>')
def fall(person):
    fall_url = base_url + 'send_ign&ign=' + str(person)
    requests.get(fall_url)
    return(render_template('realsuccess.html'))
    
@real.route('/door',methods=['POST'])
def door():
    door_url = base_url + 'send_people&people=' + request.form['people']
    requests.get(door_url)
    return(render_template('realsuccess.html'))
    
@real.route('/heart',methods=['POST'])
def heart():
    heart_url = base_url + 'send_heart&info=' + request.form['heart']
    requests.get(heart_url)
    return(render_template('realsuccess.html'))