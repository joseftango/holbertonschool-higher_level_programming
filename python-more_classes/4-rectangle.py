#!/usr/bin/python3
"""1-rectangle module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method that calculates area"""
        return self.height * self.width

    def perimeter(self):
        """method that calculates the perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """returns a string rectangle with the character #"""
        res = ''
        if self.height == 0 or self.width == 0:
            return res

        for i in range(self.height):
            for j in range(self.width):
                res += '#'
            if i != self.height - 1:
                res += '\n'

        return res

    def __repr__(self):
        """return a string representation of the
        rectangle to be able to recreate a new instance"""
        return f'{type(self).__name__}({self.width}, {self.height})'
