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
        if isinstance(value, int) or isinstance(value, float):
            if value < 0:
                raise ValueError('size must be >= 0')
            self.__size = value
        else:
            raise TypeError('size must be a number')

    def __eq__(self, value):
        return self.area() == value.area()

    def __ne__(self, value):
        return self.area() != value.area()

    def __lt__(self, value):
        return self.area() < value.area()

    def __le__(self, value):
        return self.area() <= value.area()

    def __gt__(self, value):
        return self.area() > value.area()

    def __ge__(self, value):
        return self.area() >= value.area()
