# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:38:02 2019

@author: mluci
"""

import unittest
from ch03_isprime import is_prime


#unittest.TestCase.assertTrue(is_prime(5))

class PrimesTestCase(unittest.TestCase):   
    """Tests for 'primes.py'"""   
    def test_is_five_prime(self):      
        self.assertTrue(is_prime(5.3))
    
    
    
    
if __name__ == '__main__':   
    unittest.main()