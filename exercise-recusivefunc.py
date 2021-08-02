# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:40:04 2021

@author: Pravin

Recursion example- factorial
============================
    Recursion limt is set to avoid the depth isssue or memory issues.
    We can manually set and get the recursion limts like this setrecursionlimit(lmt)
    
    WARNING
    =======
    If the purpose of the decorator was related to some kind of system management such as
    synchronization or locking, recursion is something probably best avoided.

"""

from sys import getrecursionlimit,setrecursionlimit

print(__doc__)
def factorial(n):
    """Computes n factorial. For example:
    >>> factorial(6)
    120
    >>>
    """
    if n <= 1: return 1
    else: return n * factorial(n - 1)
    
print("Current recursion limit is "+str(getrecursionlimit()))
num = int(input("Please enter the factorial number :"))
lmt = int(input("PLease enter the recursion limit :")) 
recursion_limit = int(getrecursionlimit())
while True:
    if lmt < recursion_limit:
        break
    else:
        lmt = input("PLease enter valid recusion limit :")
setrecursionlimit(lmt)
print("Setting the recursion limit, setrecursionlimit()" + str(getrecursionlimit()))
print("Factorial value is : "+str(factorial(num)))