#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_res = []
    for n in my_list:
        if n % 2 == 0:
            list_res.append(True)
        else:
            list_res.append(False)
    return list_res
