#!/usr/bin/python3
""" class that define Square """


class Square:
    """ class named Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print square method"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[0] > 0:
                for i in range(self.__position[0]):
                    print(" ", end="")
            for i in range(self.__size):
               print("#", end="")
            print()

    @property
    def position(self):
        """position getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method"""
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")        
        else:
            self.__position = value
            return self.__position
