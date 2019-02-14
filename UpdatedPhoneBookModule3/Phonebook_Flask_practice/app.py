# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:27:03 2019

@author: mluci
"""

from flask import Flask, render_template
from phonebook_functions import *


app=Flask (__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/people')
def show_people():
    people = getPeople()
    return render_template("people.html", ppl=people)
    
if __name__ == '__main__':
    app.run()