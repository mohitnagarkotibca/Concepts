# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 08:29:01 2020

@author: HP
"""
from flask import Flask,render_template

app= Flask(__name__,template_folder='templates')

posts= [
        {'name':'Mohit Nagarkoti',
         'phone_number':'1238'},
        {'name': 'Pooja Nagarkoti',
         'phone_number':'1239'},
        {'name':'Geeta Nagarkoti',
         'phone_number':'1283'}
        ]

@app.route('/')
def home():
    return render_template('home.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',posts= posts,title='home')

if __name__ == '__main__':
    app.run(debug=False,port= 8080)