#!/usr/bin/python3
"""Base module
defines the base class for Rectangle and Square to inherit from
"""
import json
from . import rectangle


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries in [None, []]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs in [None, []]:
            with open(f'{cls.__name__}.json', 'w', encoding='UTF-8') as f:
                f.write('[]')
        else:
            new_list = []

            for obj in list_objs:
                new_list.append(obj.to_dictionary())

            json_str = cls.to_json_string(new_list)

            with open(f'{cls.__name__}.json',
                      'w', encoding='UTF-8') as f:
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string in [None, '[]']:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        my_obj = rectangle.Rectangle(10, 10)
        my_obj.update(**dictionary)
        return my_obj
