#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    for i in my_list:
        if i == search:
            list.append(replace)
        else:
            list.append(i)
    return list
