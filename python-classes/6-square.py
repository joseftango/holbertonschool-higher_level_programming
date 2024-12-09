#!/usr/bin/python3
"""2-square module"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """constractor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and\
            isinstance(value[0], int) and isinstance(value[1], int)\
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """print the square using # character"""
        x = self.position[0]
        y = self.position[1]
        if self.__size == 0:
            print()
        else:
            for i in range(y):
                print()
            for r in range(0, self.__size):
                for i in range(x):
                    print(' ', end='')
                for c in range(0, self.__size):
                    print('#', end='')
                print()
