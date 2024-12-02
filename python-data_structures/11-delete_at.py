#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    max_idx = len(list) - 1
    if idx > max_idx or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
