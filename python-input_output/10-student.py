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
        my_dict = dict()

        if type(attrs) is list:
            for elem in attrs:
                if type(elem) is not str:
                    return self.__dict__

                if elem in self.__dict__:
                    my_dict[elem] = self.__dict__[elem]

            return my_dict

        return self.__dict__
