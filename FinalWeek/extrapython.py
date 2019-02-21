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
#a= ['a', 'b', 'c']
#next(a) #cant iterate over a list
#next(iter(a)) #iter will allow you to iterate
#a = iter(a)
#a
#
####### for loop ######
#a = ['a']
#for i in range(100000):
#    pass
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
#def farm_animals():
#    yield 'sheep' 
#    yield 'cow'
#    yield 'horse'
#    yield 'pig' #yield tells python its not a func but a generator and can be iterated over
#    
#animals = farm_animals
#print(animals)
#<function farm_animals at 0x0000023DDD461268> -- memory address
#next(animals) #one by one 
#for animal in animals:
#    print(animal) #all in one go    
#    
#def farm_animals2():
#    for i in range(100):
#        yield i





##### functions ####
#def bakery(cake='scone'):
#    print(cake)
#def bakery2(cake='gingerbread man'):
#    print(cake)
#    
#def bakery3(cake='gingerbread man'. workers): #wrong, keyword arguments before positional arguments


def get_data_from_sit(d):
    for item in d:
        print(item)
        
        
def get_data(**kwargs):
    for item in kwargs:
        print(item)
    
    

##### dunder methods ####
#dir(x) # find out __ commands
#class TestClass():
#    """this is a test class""""
#    
#t = TestCase()
#t=TestClass()
#t.__doc__ < #can make documentation for your class
    
    
class TestClass():
    """this is a test class"""
    def __repr__(self):
        return "Test  Class"
    def __str__(self):
        return "test for user"
    def __len__(self):
        return 5
    def __init__(self, size):
        self.size = size
    
print(t) #prints repr
t =TestClass() 
print(t)#prints str
t = TestClass(5)
len(t)
    
    
    
    
    
    
    
    
    
    
    