#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    wanted_keys = []
    for k in a_dictionary.keys():
        if a_dictionary[k] == value:
            wanted_keys.append(k)
    for wk in wanted_keys:
        del a_dictionary[wk]
    return a_dictionary
