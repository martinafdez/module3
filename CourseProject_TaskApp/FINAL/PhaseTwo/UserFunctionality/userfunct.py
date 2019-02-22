# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:18:40 2019

@author: mluci
"""
import sqlite3


conn = sqlite3.connect('TaskApp.db') 
c = conn.cursor()

def user_data():
    name = input("Enter your name: ")
    surname = input ("enter your surname: ")
    email = input("enter your email: ")
    conn = sqlite3.connect('TaskApp.db') 
    c = conn.cursor()
    c.execute('INSERT INTO users(nameUser, surnameUser, emailUser) VALUES (?,?,?)', (name, surname, email))
              
user_data()

def tasks_data():
    task = input("Enter your task: ")
    date = input ("enter your deadline: ")
    priority = input("enter the priority: ")
    status = input("enter the status of the task: ")
    description = input("enter the description: ")
    conn = sqlite3.connect('TaskApp.db') 
    c = conn.cursor()
    c.execute('INSERT INTO tasks(task, date, priority, status, description) VALUES (?,?,?, ?, ?)', (task, date, priority, status, description))
    again = input("want to add another task? Y or N?: ")
    if again == 'Y':
        user_data()
    elif again == 'N':
        pass
    

tasks_data()


             
conn.commit()
c.close()
conn.close()