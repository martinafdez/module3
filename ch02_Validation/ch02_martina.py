#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:53:55 2019

@author: martinafernandez
"""

##########Chapter 2: Validation###########


####Book tasks: Revising user inputs ####
#print("What’s your age?")
#Age = input()
#
#print ("What’s your age?")
#age = int(input())
#type(age)
#
#Option = input("Please input yes or no ").lower()
#
###Task 1#####
print("\n *--------Task 1: An example for validating string length--------* \n")

password = (input("Please enter your password: "))
print(password)

if len(password) > 4:
    print("Password too long. Try again")
elif len(password) < 4:
    print("Password too short. Try again")
else:
    print("Success. Continue!")
#    
#    
#    
###Task 2#####  

print("\n *--------Task 2: Using while true infinite loop--------* \n")

print('***choice****')
print('1. Display my name')
print('2. Display my age')
print('3. Display my city')

choice=0
while choice < 1 or choice > 3:   
    choice = int(input('What is your choice? '))

if choice == 1:   
    print('Ms Wu')
elif choice == 2:   
    print('5 years old')
elif choice == 3:   
    print('London')
#    

####Book task: Handling errorful input####
print('***choice****')
print('1. Display my name')
print('2. Display my age')
print('3. Display my city')

choice=0
while True: 
    try:      
        while choice < 1 or choice > 3:         
            choice = int(input('What is your choice? '))         
        break     
    except ValueError:      
        print('please type a number!')
        
if choice == 1:   
    print('Ms Wu')
elif choice == 2:   
    print('5 years old')
elif choice == 3:   
    print('London')



###Book task: Further on validation######
class Spam(object):   
    def __init__(self, description, value):      
        if not description or value <= 0:         
            raise ValueError      
        self.description = description      
        self.value = value
        
number=int(input("enter spam description: "))
s = Spam('s', number)
print(s.value)
