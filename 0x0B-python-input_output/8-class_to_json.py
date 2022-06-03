#!/usr/bin/python3
"""function that returns the dictionary description"""


def class_to_json(obj):
    """function that return dictionary discription"""
    return  sorted(obj.__dict__)
