#!/usr/bin/python3
from audioop import reverse


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for ele in my_list:
        print(f"{ele:d}")
