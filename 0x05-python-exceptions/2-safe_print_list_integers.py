#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if (type(i) is not int):
                continue
            if (count < x):
                print("{:d}".format(i), end="")
                count += 1
        print()
        return count
    except (TypeError, ValueError):
        pass
