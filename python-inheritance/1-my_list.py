#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    '''MyList class'''
    def print_sorted(self):
        '''prints the sorted
        list in ascending order'''
        print(sorted(self))
