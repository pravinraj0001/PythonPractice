# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:26:59 2021

@author: Pravin
"""
from datetime import date

class Foo(object):
    @staticmethod
    def add(x,y):
        return x + y
        
x = Foo.add(3,4) # calling static method
print(x)

class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():
        t = date.today()
        return Date(str(t.year),str(t.month),str(t.day))
    @staticmethod
    def tomorrow():
        t = date.today()
        return Date(str(t.year),str(t.month),str(t.day))

# Example of creating some dates
a = Date(1967, 4, 9)
b = Date.now() # Calls static method now()
c = Date.tomorrow() # Calls static method tomorrow()    
print(f'{a}\n{b}\n{c}')  