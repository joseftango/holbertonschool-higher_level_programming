#!/usr/bin/python3
"""this is a function"""


def write_file(filename="", text=""):
    """function that write a string in file and
return the number of charcatere printed"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
