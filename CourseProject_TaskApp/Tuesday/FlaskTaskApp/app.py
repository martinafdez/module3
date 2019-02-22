# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:18:30 2019

@author: mluci
"""

from flask import Flask, render_template, request, jsonify, flash, url_for, redirect
from flask_cors import CORS
from forms import LoginForm
from forms import RegistrationForm
import sqlite3

from engine import *
from engine import anotherTask, deleteTask, resultsDictionary
conn = sqlite3.connect('TaskApp.db') 
c = conn.cursor()

app=Flask (__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
cors = CORS(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.email.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Forms(form.firstname.data, form.email.data,
                    form.surname.data)
 #       db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
  
  
if __name__ == '__main__':
   app.run(debug=True)
   