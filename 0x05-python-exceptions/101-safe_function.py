#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])

    except ZeroDivisionError as err:
        sys.stderr.write(f"Exception: {err}\n")
        return None
    except TypeError as err1:
        sys.stderr.write(f"Exception: {err1}\n")
        return None
    except IndexError as err2:
        sys.stderr.write(f"Exception: {err2}\n")
        return None
