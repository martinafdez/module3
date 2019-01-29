# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:14:35 2019

@author: mluci
"""

import sqlite3
import os

###check db is exists###
def check_db(db_path):
    if os.path.exists(db_path):
        return True 
    else:
        return False
    
###Check if database is empty####
def empty_db():
    con = sqlite3.connect('hello.db')
    cursor = con.cursor()
    try:
        try: 
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print(cursor.fetchall())
               
#        except DatabaseError:
#             print(cursor.fetchall())
##            if len(cursor.fetchall()) == 0:print("got here ok")
##            return None
#    except NameError:
#        print("help")
#        return None

  #  print(cursor.fetchall())
#    if len(cursor.fetchall()) == 0:
#        return None
    
empty_db()



##connect to the database##
def getdb():
    try: 
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        return c
    except: 
        return False
#
#   
###business type##
#def typePostcode():
#    c = getdb()
#    conn=getdb()
#    userInputPostcode = input("Type in the postcode: ").upper()
#
#    while len(userInputPostcode) < 6 or len(userInputPostcode)>8:
#        try:
#            print("Please enter full postcode")
#            userInputPostcode = input("Type in the postcode: ").upper()
#
#        except  len(userInputPostcode) == 3 or len(userInputPostcode) == 2:
#            print("Please enter both parts of the postcode")
#            userInputPostcode = input("Type in the postcode: ").upper()
#
#    
#    c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcode,) )
#
#    resultsPC = c.fetchall()
#
#    if len(resultsPC ) == 0:
#        print("Sorry, nothing for this postcode! Try again.")
#        typePostcode()
#    else:
#        typeBizType(userInputPostcode) 
#        c.close()
#        conn.close()
#        
#   
#def typeBizType(userInputPostcode):
#    c = getdb()
#    conn=getdb()
#    userInputBizType = input("Type in biz type: ").title()
#    c.execute('SELECT * FROM business WHERE typeBusiness = ?', (userInputBizType,) )
#    resultsBT = c.fetchall()
#    
#    if len(resultsBT ) == 0:
#        print("Sorry, we have nothing! Try again.")
#        typeBizType(userInputPostcode)
#    else:
#        c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness  = ?', (userInputPostcode, userInputBizType) )
#    for row in c.fetchall():
#        print(row)
#        c.close()
#        conn.close()
#

