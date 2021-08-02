# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 19:14:36 2021

@author: Pravin
"""

class testing():
    def __init__(self,a):
        self.num = str(a)
        
    def display(self):
        print(self.num)

t = testing(3)
_iter = t.__iter__()       
for i in range(1,5):
    i = _iter.next()