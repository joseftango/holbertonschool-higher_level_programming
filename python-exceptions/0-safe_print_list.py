#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        idx = 0
        while idx < x:
            print('{:d}'.format(my_list[idx]), end='')
            idx += 1
        print()
    except Exception:
        print()
    return idx
