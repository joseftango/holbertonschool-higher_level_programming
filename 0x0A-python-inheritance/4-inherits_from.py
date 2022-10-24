#!/usr/bin/python3
"""creation of inherits_from function"""


def inherits_from(obj, a_class):
    """function that checks if object is
    an instance of class that inherited from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
