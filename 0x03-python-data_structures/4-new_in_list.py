#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_mylist = []
    for x in my_list:
        cp_mylist.append(x)
    if idx < 0:
        return cp_mylist
    elif idx > len(cp_mylist) - 1:
        return cp_mylist
    else:
        cp_mylist[idx] = element
        return cp_mylist
