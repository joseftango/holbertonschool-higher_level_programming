#!/usr/bin/python3
'''base module'''
from json import dumps, loads
import os


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''constractor method'''
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
        '''returns the list of the JSON
        string representation json_string'''
        if json_string in [None, '[]']:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with
        all attributes already set'''
        if cls.__name__ == 'Square':
            dummy = cls(10)
            dummy.update(**dictionary)
            return dummy

        dummy = cls(10, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        if not os.path.isfile(f'{cls.__name__}.json'):
            return []

        list_of_instances = []

        with open(f'{cls.__name__}.json', 'r', encoding='UTF-8') as f:
            list_of_dictionaries = cls.from_json_string(f.read())

        for d in list_of_dictionaries:
            instance = cls.create(**d)
            list_of_instances.append(instance)

        return list_of_instances
