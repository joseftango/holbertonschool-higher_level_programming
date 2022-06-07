#!/usr/bin/python3

class Base:
    """Base class
    this is the class for the Base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """__init__ that initialize instance attribute """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
