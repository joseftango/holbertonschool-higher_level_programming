#!/usr/bin/python3
'''base module'''


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            eval(type(self).__name__).__nb_objects += 1
            self.id = eval(type(self).__name__).__nb_objects
