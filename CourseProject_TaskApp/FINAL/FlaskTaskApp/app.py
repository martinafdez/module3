# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:18:30 2019
@author: mluci
"""

from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS

from taskappv5 import *
from taskappv5 import addTask, deleteTask

import sqlite3


app = Flask (__name__)
cors = CORS(app)

conn = sqlite3.connect('TaskApp.db')
c = conn.cursor()

@app.route('/')
def homepage():
   return render_template("index.html")

#@app.route('/tasks')
#def show_tasks():
#    tasks = resultsDictionary()
#    return render_template("tasks.html", tasks = tasks)

@app.route('/tasks', methods=['GET', 'DELETE'])
def show_tasks():
   if request.method == 'GET':
       tasks = resultsDictionary()
   if request.method == 'DELETE': #delete A TASK
       delete_task = deleteTask(taskId)
   return render_template("tasks.html", title="Overview of tasks", **locals())

#@app.route('/tasksoverview')
#def show_tasks_overview():    
#    return render_template("tasksoverview.html")

@app.route('/taskoverview', methods=['GET', 'DELETE'])
def task_overview():
#   if request.method == 'GET':
#       single_task = resultsDictionary()    
#   if request.method == 'DELETE': #delete A TASK
#       delete_task = deleteTask(taskId)
#   return render_template("tasksoverview.html", title="Overview of task information", **locals())    
    return render_template("taskoverview.html")

#@app.route('/addtasks')
#def add_new_tasks():    
#    return render_template("addtasks.html")

###### #add task #####
#@app.route('/api/addtasks', methods=['POST'])
#def add_new_tasks():
#   form_data = request.form
#   taskname = form_data['task']
#   result = anotherTask(taskname)
# #  result = "Task added successfully."
#   return redirect('/tasks')
##   return render_template("addtasks.html", title="Form confirmation", **locals())
   
@app.route("/addtasks")
def add_new_tasks():
    return render_template("addtasks.html", title="addtask")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    task = form_data['task']
    deadline = form_data['deadline']
    priority = form_data['priority']
    status = form_data['status']
    note = form_data['description']
    addTask(task, deadline, priority, status, note)
#    return render_template("/confirmation.html", title="Form Confirmation", **locals())
    return redirect("tasks", code=302)

@app.route("/confirmation-task-delete", methods=["POST"])
def confirmationDelete():
    form_data = request.form
    taskDelID = form_data['task-del']
    deleteTask(taskDelID) 
    return render_template("/confirmation-task-delete.html", title="Form Confirmation", **locals())
#    return 'DONE'


#@app.route("/confirmation-task-delete", methods=["POST"])
#def confirmationDelete():
#    form_data = request.form
#    taskDelID = form_data['task-del']
#    deleteTask(taskDelID)
#return render_template("/confirmation-task-delete.html", title="Form Confirmation", **locals())



@app.route("/api", methods = ['GET', 'POST'])
def index():
   if request.method == 'GET':
       task_list = resultsDictionary()
       return jsonify(task_list)    
   if request.method == 'POST':
       response = request.values.get('key')
       print(type(request.values))
       return jsonify({
               'data': response
               })

           
if __name__ == '__main__':
  app.run(debug=True)