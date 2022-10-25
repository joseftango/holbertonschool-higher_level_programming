#!/usr/bin/python3
"""module MyInt"""


class MyInt(int):
    """class named MyInt"""
    def __eq__(self, __x: object):
        return super().__eq__(__x) and False

    def __ne__(self, __x: object):
        return super().__ne__(__x) | True
