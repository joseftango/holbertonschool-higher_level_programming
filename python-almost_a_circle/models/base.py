#!/usr/bin/python3
'''base module'''
from json import dumps, dump


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

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation
        of list_objs to a file'''
        if list_objs is None:
            with open('file.json', 'w', encoding='UTF-8') as f:
                f.write('[]')
        else:
            new_list = []

            for obj in list_objs:
                new_list.append(obj.to_dictionary())

            json_str = cls.to_json_string(new_list)

            with open(f'{type(list_objs[0]).__name__}.json',
                      'w', encoding='UTF-8') as f:
                f.write(json_str)
