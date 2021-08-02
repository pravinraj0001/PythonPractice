# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:50:58 2021

@author: Pravin
"""
n = input("enter the number :")
s = "%{0}s%s".format(n)
g = '*'
for i in range(0,int(n)):
    print(s % (g,g))
    g += '*'
    