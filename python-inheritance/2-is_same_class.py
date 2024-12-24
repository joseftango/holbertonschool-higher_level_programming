#!/usr/bin/python3
'''2-is_same_class module'''


def is_same_class(obj, a_class):
    '''checks whether the object is
    an instance of the given class'''
    if type(obj) is a_class:
        return True
    return False
