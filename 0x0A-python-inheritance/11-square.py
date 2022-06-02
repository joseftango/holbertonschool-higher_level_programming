#!/usr/bin/python3
"""import Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is an inherited class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.width = size
        self.height = size

    def area(self):
        return self.height * self.width

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__,self.width, self.height)
