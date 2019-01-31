# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:06:06 2019

@author: mluci
"""

####Chapter 5: External testing tools#####
####App development file#####

class Calculator(object):
#    def add(self, x, y):
#        number_types=(int, float, complex)
#        if isinstance(x, number_types) and isinstance( y, number_types):
#       # None
#           return x + y
#        else:
#           raise ValueError
    ##Task 2: Debugging code while testing##
    #Fail version#
    def add(self, x, y):
        number_types=(int, float, complex)
        if isinstance(x, number_types) and isinstance( y, number_types):
            import pdb; pdb.set_trace() #new debugging technique
            result = x-y
            print('Result is: {}'.format(result))
            return result
        else:
            raise ValueError
        
    
        
