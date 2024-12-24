#!/usr/bin/python3
'''7-base_geometry module'''


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        '''raises an Exception with message'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''that validates value'''
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
