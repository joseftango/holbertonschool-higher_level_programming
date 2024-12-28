#!/usr/bin/python3
'''100-append_after module'''


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        lines_cp = lines.copy()
    res = []
    for i in range(len(lines)):
        if search_string in lines[i]:
            res.append(lines[i])
            res.append(new_string)
        else:
            res.append(lines[i])

    my_str = ''
    for s in res:
        my_str += s
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(my_str)
