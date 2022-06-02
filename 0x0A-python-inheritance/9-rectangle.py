#!/usr/bin/python3
"""import class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is an inherited class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        a = self.__height * self.__width
        return a

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
