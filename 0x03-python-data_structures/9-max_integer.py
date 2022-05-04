#!/usr/bin/python3
from asyncio.windows_events import NULL


def max_integer(my_list=[]):
    if my_list == NULL:
        return None
    max = my_list[0]
    for x in my_list:
        if x > max:
            max = x
    return max
