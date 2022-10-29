#!/usr/bin/python3
"""writing a class named Base"""
import json
import os.path
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

    @staticmethod
    def from_json_string(json_string):
        """method that return a list of the json string representation """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with
        all attributes already set"""
        if dictionary is None:
            return None
        dummy = cls(2, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        li = []
        if os.path.exists(f'{cls.__name__}.json'):
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
            for i in data:
                li.append(cls.create(**i))
        return li
