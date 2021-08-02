# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:22:00 2021

@author: Pravin
"""
class Vechile:
    def __init__(self,vechile_type):
        self.vechile_type = vechile_type
    
    def __str__():
        return f'This is vechile class'
    
class fourwheeler(Vechile):
    def __init__(self,vechile_type,t):
        super().__init__(vechile_type)
        self.wheel = t

er = Vechile(3)
print(er.vechile_type)
vech = fourwheeler(4,3)
print(vech)