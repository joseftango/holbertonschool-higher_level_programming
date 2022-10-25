#!/usr/bin/python3
"""add_attribute model"""


def add_attribute(object, at1, name):
    """function that adds new attribute to an object"""
    if type(object) in (int, float, str, bool, tuple, set, list, dict):
        raise TypeError("can't add new attribute")

    object.at1 = at1
    object.name = name
