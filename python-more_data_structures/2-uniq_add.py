#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    my_list = list(set(my_list))
    acc = my_list[0]
    for i in range(1, len(my_list)):
        acc += my_list[i]
    return acc
