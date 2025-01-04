#!/usr/bin/python3
'''base module'''
from json import dumps


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
        '''returns the JSON string
        representation of list_dictionaries'''
        if list_dictionaries in [None, []]:
            return "[]"
        return dumps(list_dictionaries)
