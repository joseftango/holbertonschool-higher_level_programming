#!/usr/bin/python3
"""Rectangle module
This module defines a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    this is the class for rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method
        this method initializes on instance creation
        """
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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that calculates the area of rectangle"""
        return self.height * self.width

    def display(self):
        """method that prints rectangle """
        for x in range(self.y):
            print()
        for i in range(self.height):
            for y in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ method
        print the rectangle on print() or str()
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update Method
        this method will assign a key/value argument to attributes
        """
        argc = len(args)
        my_list = ["id", "width", "height", "x", "y"]
        if argc > 0:
            if argc > len(my_list):
                argc = len(my_list)
            for i in range(argc):
                setattr(self, my_list[i], args[i])
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method that return a dictionary representation of the class"""
        return {'x': self.x, 'y': self.y, 'id':
                self.id, 'height': self.height, 'width': self.width}
