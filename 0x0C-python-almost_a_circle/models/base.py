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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that return a json string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file: writes the json string representation of list_objs"""
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([i.to_dictionary()
                        for i in list_objs]))
