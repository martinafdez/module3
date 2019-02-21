# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:37 2019

@author: mluci
""" 

import unittest
from database_creation import *



class DatabaseTest(unittest.TestCase):            
    #unit test for connecting#
    def test_connect_db(self):
        self.assertTrue(getdb('TaskApp.db'))
    #unit test for whether database exists#
    def test_check_db(self):
        self.assertTrue(check_db("TaskApp.db"))
    #check if database is empty#
    def test_empty_db(self):
        self.assertTrue(checkIfTables('TaskApp.db'))  
    #check if tables in database are empty#
    def test_empty_table_users(self):
        self.assertTrue(checkIfUsersTableEmpty('TaskApp.db')) 
    def test_empty_table_tasks(self):
        self.assertTrue(checkIfTasksTableEmpty('TaskApp.db'))

   
    
    
if __name__ == '__main__':   
    unittest.main()