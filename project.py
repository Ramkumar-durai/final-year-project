from flask import Flask, render_template, flash, request, session,Response
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename

import mysql.connector

import os
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.config['DEBUG']


@app.route("/")
def homepage():
    return render_template('login.html')


@app.route("/adminhome")
def adminhome():

    return render_template('adminhome.html')

@app.route("/iotdata")
def iotdata():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='manhole')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM iotdata ORDER BY id DESC LIMIT 10")
    data = cur.fetchall()
    return render_template('iotdata.html',data=data)



@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' and request.form['password'] == 'admin':


           return render_template('AdminHome.html')

       else:

           alert = 'Username or Password is wrong'
           return render_template('goback.html', data=alert)






@app.route('/logout')
def logout():


    return render_template('login.html')


@app.route("/map")
def map():
    lat=request.args.get('lat')
    lng = request.args.get('long')



    return render_template('map.html',lat=lat,lng=lng)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)