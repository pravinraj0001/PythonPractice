# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:02:31 2021

@author: Pravin
"""

class Book:
    TYPES = ("hardcover","paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}gm>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight + 100)
    
    
book = Book.hardcover("Sapiens",1000)
light = Book.paperback("Zero to One",600)

print(Book)

print(book)
print(light)