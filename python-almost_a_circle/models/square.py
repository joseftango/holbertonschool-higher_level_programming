#!/usr/bin/python3
'''square module'''
from models import rectangle


class Square(rectangle.Rectangle):
    '''Square class inherits from rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id})\
 {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''assigns an args and kwargs
        to the respective attributes'''
        if args and len(args) > 0:
            my_keys = ['id', 'size', 'x', 'y']
            i = 0
            while i in range(len(args)):
                for k in my_keys[:len(args)]:
                    setattr(self, k, args[i])
                    i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        my_dict = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return my_dict
