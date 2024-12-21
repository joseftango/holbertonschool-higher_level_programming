#!/usr/bin/python3
'''LockedClass Module'''


class LockedClass:
    '''LockedClass Class'''
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__['first_name'] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
