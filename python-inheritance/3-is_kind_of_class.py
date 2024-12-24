#!/usr/bin/python3
'''3-is_kind_of_class module'''


def is_kind_of_class(obj, a_class):
    '''cheks if object is an instance of class
    or instance of a class that inherited from'''
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    return False
