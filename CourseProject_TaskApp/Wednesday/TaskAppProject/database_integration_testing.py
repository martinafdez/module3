# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 10:04:20 2019

@author: mluci
"""

####Integration testing for phonebook project####
from database_creation import *

class TestEngine():
    #testing if database exists#
    def test_exists(self):
        self.checked=check_db('TaskApp.db')
        if self.checked:
            return True
        else:
            return False
    
    #testing if connection function is working#
    def test_getdb(self):
        self.test_exists()
        if self.checked:
            connected=getdb('TaskApp.db')
            if connected:
                self.connected = True
                print("Success.")
                return self.connected
            else:
                self.connected = False
                print("No success.")
                return self.connected
        else:
            print("Database Does Not Exist")
    
        #testing if database is empty#
    def test_databaseEmpty(self):
        self.test_getdb()
        if self.connected:
            checkEmptyDb=checkIfTables('TaskApp.db')
            if checkEmptyDb:
                self.checkEmptyDb = True
                print("Tables exist.")
                return self.checkEmptyDb
            else:
                self.checkEmptyDb = False
                print("No tables.")
                return self.checkEmptyDb
        else:
            print("Database did not connect.")
            
            
    #testing if database is empty#
    def test_UserDatabaseEmpty(self):
        self.test_databaseEmpty()
        if self.checkEmptyDb:
            checkEmptyTable=checkIfUsersTableEmpty('phonebook.db')
            if checkEmptyTable:
                self.checkEmptyTable = True
                print("Table full.")
                return self.checkEmptyTable
            else:
                self.checkEmptyTable = False
                print("Tables empty.")
                return self.checkEmptyTable
        else:
            print("Database is empty - no tables to test.")
            
        #testing if database is empty#
    def test_TasksDatabaseEmpty(self):
        self.test_databaseEmpty()
        if self.checkEmptyDb:
            checkEmptyTable=checkIfTasksTableEmpty('TaskApp.db')
            if checkEmptyTable:
                self.checkEmptyTable = True
                print("Table full.")
                return self.checkEmptyTable
            else:
                self.checkEmptyTable = False
                print("Tables empty.")
                return self.checkEmptyTable
        else:
            print("Database is empty - no tables to test.")
        
 
            
    
    
            
    def runtests(self):
        print(self.test_exists())
        print(self.test_getdb())
        print(self.test_databaseEmpty())
        print(self.test_UserDatabaseEmpty())
        print(self.test_TasksDatabaseEmpty())
        
            
if __name__ == '__main__':   
    testing=TestEngine()
    
    testing.runtests()