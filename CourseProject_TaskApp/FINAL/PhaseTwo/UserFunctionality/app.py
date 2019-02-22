# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:18:30 2019

@author: mluci
"""

from flask import Flask, render_template, request, jsonify, flash, url_for, redirect
from flask_cors import CORS
#from forms import LoginForm
#from forms import RegistrationForm

from engine import *
from engine import anotherTask, deleteTask, resultsDictionary
conn = sqlite3.connect('TaskApp.db') 
c = conn.cursor()

app=Flask (__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
cors = CORS(app)

########overview of every task######## includes delete####
@app.route('/tasks', methods=['GET', 'DELETE'])
def show_tasks():
    if request.method == 'GET':
        tasks = resultsDictionary()
    if request.method == 'DELETE': #delete A TASK 
        delete_task = deleteTask(taskId)
    return render_template("tasks.html", title="Overview of tasks", **locals())



###### ############add task ###############
@app.route('/addtasks')
def add_new_tasks():
    form_data = request.form
    taskname = form_data['task']
    result = anotherTask(taskname)
  #  result = "Task added successfully."
    return redirect('/tasks')



#@app.route('/deletetasks', methods=['POST'])
#def del_tasks():
#    form_data = request.form
#    deletetasks=form_data["delete_task"]
#    delete_task = deleteTask(deletetasks) #FUNCTION NEEDED
#    result = "Task deleted successfully."
#    return render_template("/deletetasks.html", title="Deletion of task", **locals())

@app.route('/deletetasks', methods=['POST'])
def del_tasks():
    c.execute('DELETE FROM tasks WHERE taskId = ?', [request.form['delete_task']])
    conn.commit()
    return redirect(url_for("/tasks.html"))


  
  
if __name__ == '__main__':
   app.run(debug=True)
   