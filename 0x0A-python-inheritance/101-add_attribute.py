#!/usr/bin/python3
"""add_attribute model"""


def add_attribute(object, at1, name):
    """function that adds new attribute to an object"""
    if hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")

    object.at1 = at1
    object.name = name
