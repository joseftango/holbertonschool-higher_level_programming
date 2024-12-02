#!/usr/bin/python3
def valid_tuple(tup=()):
    if len(tup) < 2:
        if len(tup) == 1:
            valid_tup = tup[0], 0
        else:
            valid_tup = 0, 0

    elif len(tup) >= 2:
        valid_tup = tup[0], tup[1]

    return valid_tup


def add_tuple(tuple_a=(), tuple_b=()):

    valid_tuple_a = valid_tuple(tuple_a)
    valid_tuple_b = valid_tuple(tuple_b)

    res1 = valid_tuple_a[0] + valid_tuple_b[0]
    res2 = valid_tuple_a[1] + valid_tuple_b[1]

    return res1, res2
