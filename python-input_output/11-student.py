#!/usr/bin/python3
'''10-student module'''


class Student:
    '''Student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation
        of a Student instance'''
        my_dict = {}

        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__

                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]

            return my_dict

        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for k, v in json.items():
            self.__dict__[k] = v
