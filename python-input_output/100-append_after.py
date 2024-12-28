#!/usr/bin/python3
'''100-append_after module'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        lines_cp = lines.copy()

    for i in range(len(lines)):
        if search_string in lines[i]:
            first = lines_cp[:i + 1]
            first.append(new_string)
            last = lines_cp[i + 1:]
            res = first + last
            break
    my_str = ''
    for s in res:
        my_str += s
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(my_str)
