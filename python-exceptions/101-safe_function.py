#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(args[0], args[1])
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as e:
        print('Exception: {}'.format(e), file=sys.stderr)
        res = None
    return res
