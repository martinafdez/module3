# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:18:30 2019

@author: mluci
"""

from flask import Flask, render_template, request, jsonify, flash, url_for, redirect
from flask_cors import CORS
from forms import LoginForm
from forms import RegistrationForm

from engine import *


app=Flask (__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
#cors = CORS(app)
#newtask= newTask()

##### log in ######
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.email.data))
        return redirect('/index')
    return render_template('index.html', title='Sign In', form=form)


##### register ######
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
#        user = User(form.username.data, form.email.data,
#                    form.password.data)
#        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)




####### display all the tasks (fab)#######
@app.route('/api/tasks', method=['POST'])  
def show_tasks():

    return render_template("tasks.html")




##### overview of all tasks (fab)#######
@app.route('/api/tasksoverview', method=['GET', 'PUT', 'DELETE'])
def show_tasks_overview():


    return render_template("tasksoverview.html")


##### #add task #####
@app.route('/api/addtasks', method=['POST'])
def add_new_tasks():
    form_data=request.form
    if request.method == 'POST': # ADD A NEW TASK 
        edit_task = editfunctionfromfile
        return render_template("/confirmation-edit.html", title="Form confirmation", **locals())

    
    return render_template("add tasks.html" )



######  display data api #######
@app.route("/api", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        display_data = resultsDictionary()
        return jsonify(display_data)
    
    if request.method == 'POST':
        response = request.values.get('key')
        print(type(request.values))
        return jsonify({
                'data': response
                })
    
    
####### delete/ edit tasks ######    
@app.route("/api<int:id>", methods = ['GET', 'POST', 'PUT', 'DELETE'])
def getdb(): #DELETE A TASK   
    if request.method == 'DELETE': #if its a get request
        delete_task = deletefunctionfromfile
        return render_template("/confirmation-delete.html", title="Form confirmation", **locals())
    
    if request.method == 'PUT': #EDIT A TASK 
        edit_task = editfunctionfromfile
        return render_template("/confirmation-edit.html", title="Form confirmation", **locals())
    
    


if __name__ == '__main__':
   app.run(debug=True)
   