#!/usr/bin/python3
"""this is a class"""


class MyList(list):
    """class named MyList"""
    def print_sorted(self):
        sorted_li = self.copy()
        sorted_li.sort()
        print(f"{sorted_li}")
