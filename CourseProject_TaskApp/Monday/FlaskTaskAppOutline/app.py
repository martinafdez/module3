# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:18:30 2019

@author: mluci
"""

from flask import Flask, render_template, request
from database_creation import *


app=Flask (__name__)


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/tasks')
def show_tasks():
    
    return render_template("tasks.html")

@app.route('/tasksoverview')
def show_tasks_overview():
    
    return render_template("tasksoverview.html")

@app.route('/addtasks')
def add_new_tasks():
    
    return render_template("addtasks.html")


if __name__ == '__main__':
   app.run(debug=True)