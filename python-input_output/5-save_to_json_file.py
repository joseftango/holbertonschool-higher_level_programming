#!/usr/bin/python3
"""5-save_to_json_file module"""
from json import dump


def save_to_json_file(my_obj, filename):
    '''function that writes an Object to a
    text file, using a JSON representation'''
    with open(filename, 'w', encoding="UTF-8") as f:
        dump(my_obj, f)
