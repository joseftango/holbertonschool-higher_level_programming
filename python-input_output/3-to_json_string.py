#!/usr/bin/python3
'''3-to_json_string module'''
from json import dumps


def to_json_string(my_obj):
    '''function that returns the JSON
    representation of an object (string)'''
    return dumps(my_obj)
