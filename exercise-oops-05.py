# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:19:30 2021

@author: Pravin
"""

class Times(object):
    factor = 1
    @classmethod
    def mul(cls,x):
        return cls.factor*x
class TwoTimes(Times):
    factor = 2
x = TwoTimes.mul(4) # Calls Times.mul(TwoTimes, 4) -> 8
print(x)