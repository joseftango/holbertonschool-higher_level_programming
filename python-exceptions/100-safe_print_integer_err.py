#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        res = True
    except (ValueError, TypeError) as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        res = False
    return res
