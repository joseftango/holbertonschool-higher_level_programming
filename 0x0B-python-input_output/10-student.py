#!/usr/bin/python3
"""this is a class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializing function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that that retrieves a dictionary representation"""
        my_dict = dict()
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__

                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return my_dict

        return self.__dict__
