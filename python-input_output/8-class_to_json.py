#!/usr/bin/python3
'''8-class_to_json module'''


def class_to_json(obj):
    '''returns the dictionary description with simple
    data structure for JSON serialization of object'''
    return obj.__dict__
