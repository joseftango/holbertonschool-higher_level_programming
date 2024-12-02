#!/usr/bin/python3
def element_at(my_list, idx):
    max_idx = len(my_list) - 1
    if idx < 0:
        return None
    if idx > max_idx:
        return None
    return my_list[idx]
