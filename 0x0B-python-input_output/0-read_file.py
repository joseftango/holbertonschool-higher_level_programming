#!/usr/bin/python3
"""this is a function"""


def read_file(filename=""):
    """function that read a txt file and print it to stdout """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
