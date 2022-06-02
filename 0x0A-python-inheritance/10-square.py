#!/usr/bin/python3
"""import Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """this is an inherited class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size

    def area(self):
        a = self.size * self.size
        return a

    def __str__(self):
        return f"[Rectangle] {self.size}/{self.size}"
