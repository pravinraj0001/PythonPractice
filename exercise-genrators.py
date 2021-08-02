# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:32:35 2021

@author: Pravin
"""

### Filter out a comments from the file
# Read the file
f = open("data.txt")
# Go through the file through generators
comments = (t fo t in lines if t[0] == '#')
for c in comments:
    print(c)