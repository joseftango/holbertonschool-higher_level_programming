#!/usr/bin/python3
"""writing a class named Rectangle"""
from models.base import Base


class Rectangle(Base):
    """this is a class
    Rectangle inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ that initialize instance attribute """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        return self.__width

    def set_width(self, value):
        self.__width = value

    @property
    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    @property
    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value
