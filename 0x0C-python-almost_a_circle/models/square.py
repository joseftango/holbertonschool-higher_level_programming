#!/usr/bin/python3
"""Square module
This module defines a Square class
"""
from models.rectangle import Rectangle
"""import rectangle model"""


class Square(Rectangle):
    """a Square class that inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = self.width

    def update(self, *args, **kwargs):
        """this method assign the key or value argument to attributes
        """
        argc = len(args)
        my_list = ["id", "size", "x", "y"]
        if argc > len(my_list):
            argc = len(my_list)
        for i in range(argc):
            setattr(self, my_list[i], args[i])
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """this method return a dictionary representation of class"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
