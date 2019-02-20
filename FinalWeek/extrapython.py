# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:11:35 2019

@author: mluci
"""
##### list comprehension #####
#def code():
#    a = ['1' '2', '3', '3']
#    b = ['a', 'b', 'c']
#    
#    for item in a:
#        c = b.append(item)
#        
#    c = [ 'x' if item % 2 == 0
#         else 'b'
#         for item in a]
#    
#    d = [ item for item in zip(a, b)]
#    print(a, b, c, d)
#
#
#    e = [i for i in range(10000000)]
#    for i in range(10000000):
#        b.append(i)
#
#
####### for loop ######
#a = ['a']
#for i in range(100000):
#    pass
#
#
#
#data = ['a','b','c']
#print(data)
#
#for i, item in enumerate(data):
#    print(i)
#
#
#x = enumerate(data)
#for idx, item in c:
#    print(idx, item)
#    
#x = enumerate(range(10000000))
#tenmillion=enumerate(range(10000000))
#x
#next(x)
#
#x = enumerate(range(2))
#next(x)    
#    


#a = [a for a in range(100)]
#next(a)    #type error, cant interate over a list



####### generators ########
def farm_animals():
    yield 'sheep' 
    yield 'cow'
    yield 'horse'
    yield 'pig' #yield tells python its not a func but a generator and can be iterated over
    
animals = farm_animals
#print(animals)
#<function farm_animals at 0x0000023DDD461268> -- memory address
#next(animals) #one by one 
for animal in animals:
    print(animal) #all in one go    
    
