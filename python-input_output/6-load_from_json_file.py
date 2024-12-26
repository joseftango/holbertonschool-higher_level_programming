#!/usr/bin/python3
"""6-load_from_json_file"""
from json import load


def load_from_json_file(filename):
    '''function that creates an Object from a JSON file'''
    with open(filename, 'r', encoding="UTF-8") as f:
        obj = load(f)
    return obj
