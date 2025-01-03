#!/usr/bin/python3
'''square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}'
