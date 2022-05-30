#!/usr/bin/python3
"""this is a function that takes a class as argument"""

def lookup(obj):
    """ function that returns a list of available attributes and methods of an object"""
    return dir(obj)
