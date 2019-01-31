# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:39:37 2019

@author: mluci
"""

####Module 3: Exceptions and validations ####

#Dealing with multiple errors#
#
try:
    f = open('testfile.txt')
    s1 = not_exist
except FileNotFoundError: #Exception : would return correct error for undefined name variable
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")

#Multiple exceptions#
try:
    f = open('testfile.txt')
    s1 = not_exist
except FileNotFoundError:
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")
except Exception:
    print("Sorry. Something is wrong after opening function.")




##Task 1##
print("\n*------Task 1------*\n")


try:
    f = open('testfile.txt')
    s1 = not_exists
except Exception as e: #e is variable that represents anything wrong.
    print(e)


##Task 2##
print("\n*------Task 2------*\n")

try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close
    
##Task 3##
print("\n*------Task 3------*\n")

#With error#
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close
finally:
    print('Executing finally...')
    
#Without error#
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close
finally:
    print('Executing finally...')   
    
    
##Task 4##
print("\n*------Task 4------*\n")   
    
try:
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print('file name are the same')