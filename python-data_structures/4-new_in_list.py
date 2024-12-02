#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    max_idx = len(my_list) - 1
    new_li = my_list[:]
    if idx < 0:
        return new_li
    if idx > max_idx:
        return new_li
    new_li[idx] = element
    return new_li
