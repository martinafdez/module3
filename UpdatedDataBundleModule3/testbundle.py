# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:56:00 2019

@author: mluci
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:06:31 2018

@author: 612383263
"""
#--------Module 2: Lesson 8---------
#----"Data Bundle Exercise"----

###Running exercise and importing functions###
from SimpleBundlePurchase import DataBundlePurchase

# Test call to programme:
print ('TEST EXAMPLE 1')
# database input, you will still need to check user pin
result = DataBundlePurchase('1234', 34.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = DataBundlePurchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = DataBundlePurchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')