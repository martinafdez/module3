# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:59:00 2019

@author: mluci
"""

##########Test driven development############

import unittest


def is_prime(number):
     if number <= 1:      
         return False   
     for element in range(2, number):      
         if number % element == 0:        
             return False   
     return True