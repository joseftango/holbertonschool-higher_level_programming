#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [True if i % 2 == 0 else False for i in my_list]

# def divisible_by_2(my_list=[]):
# 	return list(map(lambda x: True if x % 2 == 0 else False), my_list)
