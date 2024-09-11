#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1 = set_1
    s2 = set_2
    return [i for i in s1 if i in s2]
