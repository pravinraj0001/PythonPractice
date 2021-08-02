# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:20:54 2021

@author: Pravin
"""

#class in Flask exercise

class Student:
    def __init__(self,rank):
        self.name = "Pravin"
        self.grades = (90,79,83,72)
        self.rank = rank
    def average(self):
        return sum(self.grades)/len(self.grades)
    
    '''def __str__(self):
        return "Hello"'''
    def __repr__(self):
        return f"<Student({self.name})>"
    
student = Student(rank = 14)
final = student.name,student.grades,student.rank
print(final)
print("{}".format(student.average()))
print(student)