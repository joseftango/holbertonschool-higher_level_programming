#!/usr/bin/python3
'''10-square module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        super().__init__(size, size)
