#!/usr/bin/python3
"""this is a function"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
