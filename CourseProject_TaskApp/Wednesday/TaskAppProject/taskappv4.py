# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:07:52 2019

@author: iza
"""

#creating api = create a json datablock that represents a database 
# next:
## jsonify
## input validation 

import sqlite3 
import json

# 
class newTask(object):

    def __init__(self, task, userID):
        self.task = task
        self.userID = userID
        
    def addDeadline(self):
        deadline = input("What's the deadline? ")
        self.deadline = deadline
        return self.deadline
    
    def addPriority(self):
        priority = input("What's the priority? 1-high, 2-low. ")
        if priority == "1":
            self.priority = "High"
        elif priority== "2":
            self.priority ="Low"
        return self.priority


    def addStatus(self):
        status = input("What's the status? 1 - To do, 2 - In progress, 3 - Done. ")
        if status == "1":
            self.status = "To do"
        elif status == "2":
            self.status = "In progress"
        elif status == "3":
            self.status = "Done"
        print(self.status)
        return self.status
    
    def addNote(self):
        note = input("Add a note: ")
        self.note = note
        return self.note 
        


    def taskSummary(self):
        print("Task: " + self.task)
        print("Deadline: " + self.deadline)
        print("Priority: " + self.priority)
        print("Status: " + self.status)
        print("Note: " + self.note)
#        self.taskID = 1
#    

        print("User ID: " + self.userID)
        conn = sqlite3.connect('TaskApp.db') 
        c = conn.cursor()
        
        c.execute('INSERT INTO tasks(userID, task, date, priority, status, description) VALUES (?,?,?,?,?,?)', (self.userID, self.task, self.deadline, self.priority, self.status, self.note))
    
        conn.commit()
        c.close()
        conn.close()
        
def typeTask():
    #this will be gone in flask 
    task = input("What's the task? ")
    return task 

def anotherTask():
    addAnotherTask="Y"
    while addAnotherTask == "Y":  
        task = typeTask()
        addTask(task)        
        addAnotherTask = input("Add another task? Y or N. ")
    else:
        pass

        
def addTask(task):
        userID = "abc123"
        Task1 = newTask(task, userID)
        Task1.addDeadline()
        Task1.addPriority()
        Task1.addStatus()
        Task1.addNote()
        
        print()
        Task1.taskSummary()
        


def resultsDictionary():
    results = {}
    conn = sqlite3.connect('TaskApp.db') 
    c = conn.cursor()
    
    c.execute('SELECT * FROM tasks')
    resultsDb =  c.fetchall() 
    print("RESULTS_DB")
    print(resultsDb)
    print()

    for row in resultsDb : 
        key = row[2]
        value = row[3:]
        results [key] = (value)

    print(results)
    c.close()
    conn.close()
    
