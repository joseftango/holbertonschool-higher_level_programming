#!/usr/bin/python3
"""creation of class Square"""


class Square:
    """class named Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializing function"""
        self.__size = size
        self.__position = position

    def area(self):
        """retrive area of square"""
        res = self.__size ** 2
        return res

    @property
    def size(self):
        """size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) == tuple and len(value) == 2\
                and type(value[0]) == int and type(value[1]) == int:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value

        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """my_print method"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for p in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
