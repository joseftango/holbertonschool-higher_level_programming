#!/usr/bin/python3
"""2-square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """constractor"""
        self.size = size

    def area(self):
        """method that computes square area"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
