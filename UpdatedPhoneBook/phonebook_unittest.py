# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:37 2019

@author: mluci
""" 

import unittest
from unittest import mock
from funct2 import *



class DatabaseTest(unittest.TestCase):
#     @mock.patch('funct2.input', create=True)
#     def testdictCreateSimple(self, mocked_input):
#        mocked_input.side_effect = ['N3 1AA', 'LS6 1AD', 'OX7 3AA']
#        result = typePostcode()
#        self.assertEqual(result, 'N3 1AA')
            
    #unit test for connecting#
    def test_connect_db(self):
        self.assertTrue(getdb('empty_database.db'))
    #unit test for whether database exists#
    def test_check_db(self):
        self.assertTrue(check_db("empty_database.db"))
    #check if database is empty#
    def test_empty_db(self):
        self.assertTrue(checkIfTables('empty_database.db'))  
    #check if tables in database are empty#
    def test_empty_table(self):
        self.assertTrue(checkIfTableEmpty('empty_database.db')) 
  

   
    
    
if __name__ == '__main__':   
    unittest.main()