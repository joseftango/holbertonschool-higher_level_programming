#!/usr/bin/python3
'''101-add_attribute module'''


def add_attribute(obj, attr_name, attr_value):
    """function that adds a new attribute
    to an object if it's possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
