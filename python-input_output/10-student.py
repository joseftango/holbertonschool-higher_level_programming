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
        Keys = list(self.__dict__.keys())
        full_dict_sorted = {i: self.__dict__[i] for i in sorted(Keys)}

        if not attrs:
            return full_dict_sorted

        if type(attrs) is list:
            only_attrs_dict = {}
            for i in sorted(attrs):
                if type(i) is not str:
                    return full_dict_sorted
                if hasattr(self, i):
                    only_attrs_dict[i] = getattr(self, i)
            return only_attrs_dict

        return full_dict_sorted
