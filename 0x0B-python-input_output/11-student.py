#!/usr/bin/python3
"""creation of student class"""


from subprocess import list2cmdline


class Student:
    """class named Student"""
    def __init__(self, first_name, last_name, age):
        """initializing function of multipule data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that returns a dictionary representation"""
        return self.__dict__

    def to_json(self, attrs=None):
        "returns a dictionary representation of specefic attribute"
        if type(attrs) == list:
            d = dict()
            for k, v in sorted((self.__dict__).items()):
                for j in attrs:
                    if type(j) != str:
                        return self.__dict__
                    if j == k:
                        d[k] = v
            return d

        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
