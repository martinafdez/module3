# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:17:37 2019

@author: mluci
""" 

import unittest
from funct2 import *





class DatabaseTest(unittest.TestCase):
#    def test_check_db(self):
#        self.assertTrue(check_db("phonebook.db"))
    
    
    def test_empty_check_db(self):
        self.assertIsNone(empty_db())    
  

   
    
    
if __name__ == '__main__':   
    unittest.main()