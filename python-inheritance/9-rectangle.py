#!/usr/bin/python3
'''9-rectangle module'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class'''
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''calculates the area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''magic method'''
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
