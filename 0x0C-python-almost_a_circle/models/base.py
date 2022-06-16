#!/usr/bin/python3
"""writing a class named Base"""
import json
"""import a json module"""


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

    def to_json_string(list_dictionaries):
        """method that return a json string representation"""
        if list_dictionaries is None :
            return "[]"
        return json.dumps(list_dictionaries)
