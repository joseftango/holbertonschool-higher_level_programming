#!/usr/bin/python3
'''4-from_json_string module'''
from json import loads


def from_json_string(my_str):
    '''function that returns an object
    represented by a JSON string'''
    return loads(my_str)
