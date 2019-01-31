# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:10:28 2019

@author: mluci
"""

####Chapter 5: External testing tools#####
####Test file#####

import unittest
from ch05_martina_functions import Calculator

###Task 1###

class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc=Calculator()
    def test_calculator_add_method_returns_correct_result(self):
        #calc=Calculator()
        result= self.calc.add(2, 2)
        self.assertEqual(4, result)
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
            
        
if __name__ == '__main__':
    unittest.main()
    
    
#navigate to dir on command line and run nosetests FILE_NAME.py    
           