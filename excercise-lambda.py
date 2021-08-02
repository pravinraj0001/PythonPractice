# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:11:43 2021

@author: Pravin
"""

""" Lambda functions exercise using lambda operator """
a = lambda x,y : x+y
r = a(2,3)
print(r)

names = ['Sheldon','Damian','John','Harrold']
print('Before sort :' +str(names))
names.sort(key=lambda n: n.lower())
print('After sort : '+str(names))
