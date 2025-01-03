#!/usr/bin/python3
'''rectangle module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''calculates the area of rectangle'''
        return self.width * self.height

    def display(self):
        '''prints in stdout the Rectangle
        instance with the character #'''
        for abssica in range(self.y):
            print()
        for r in range(self.height):
            for ordinate in range(self.x):
                print(' ', end='')
            for c in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        '''assigns an args and kwargs to the respective attributes'''
        if args and args == ():
            my_keys = ['id', 'width', 'height', 'x', 'y']
            i = 0
            while i in range(len(args)):
                for k in my_keys[:len(args)]:
                    setattr(self, k, args[i])
                    i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
