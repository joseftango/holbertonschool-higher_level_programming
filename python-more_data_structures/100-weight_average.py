#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res1 = 0
    res2 = 0
    for x, y in my_list:
        res1 += x * y
        res2 += y
    return res1 / res2
