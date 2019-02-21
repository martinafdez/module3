# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:28:56 2019

@author: mluci
"""

import sqlite3 
import json
import random
import requests
import os



############### Database connection #####################
conn = sqlite3.connect('TaskApp.db') 

c = conn.cursor()

########### Database testing #####################

def getdb(db_file):
    try: 
        conn = sqlite3.connect('TaskApp.db')
        c = conn.cursor()
        return c
    except: 
        return False
    
    
###-check if database exists-###
def check_db(db_file):
    if os.path.exists(db_file):
        return True 
    else:
        return False
    
    
###-Check if database is empty-####
def checkIfTables(db_file):
    c=getdb(db_file)
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablesInDb =(c.fetchall())
    print(len(tablesInDb))
    print(tablesInDb)
    if len(tablesInDb) > 0:
        print("Tables available.")
        return True
    else:
        print("table unavailable")
        return False
    #dbClose(db_file)

####-Check if tables in database are empty-###
def checkIfUsersTableEmpty(db_file):
    try:
        c = getdb(db_file)
        c.execute('SELECT * FROM users')
        resultsRecords = c.fetchall()
        if len(resultsRecords ) > 0:
            print("Table not empty")
            return True
        else:
            print("Table is empty")
            return False
    except sqlite3.OperationalError:
        print("Table doesn't exist. Can't run check.")
        
    
    
    #dbClose(db_file)
    
def checkIfTasksTableEmpty(db_file):
    try:
        c = getdb(db_file)
        c.execute('SELECT * FROM tasks')
        resultsRecords = c.fetchall()
        if len(resultsRecords ) > 0:
            print("Table not empty")
            return True
        else:
            print("Table is empty")
            return False
    except sqlite3.OperationalError:
        print("Table doesn't exist. Can't run check.")
        
    
    
    #dbClose(db_file)

    


############### CREATE USERS TABLE ######################
def create_table_user():
    c.execute('CREATE TABLE IF NOT EXISTS users(userId INTEGER PRIMARY KEY AUTOINCREMENT, nameUser TEXT, surnameUser TEXT, emailUser VARCHAR(255))')
    
    
############### CREATE TASKS TABLE #####################
def create_table_tasks():
    c.execute('CREATE TABLE IF NOT EXISTS tasks(userId REFERENCES users(userId), taskId INTEGER PRIMARY KEY AUTOINCREMENT, task VARCHAR(255), date DATETIME, priority TEXT, status TEXT, description VARCHAR (255))')

create_table_user()
create_table_tasks()
      

######### CLOSE DATABASE #############           
c.close()
conn.close()   
    
    
    
    