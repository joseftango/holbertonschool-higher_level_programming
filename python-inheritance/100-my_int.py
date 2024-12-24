#!/usr/bin/python3
"""100-my_int module"""


class MyInt(int):
    '''MyInt class'''
    pass

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
