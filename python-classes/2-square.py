#!/usr/bin/python3
"""2-square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """constractor"""
        if type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
