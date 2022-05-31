#!/usr/bin/python3
"""this is a function"""


def append_write(filename="", text=""):
    """function that append a string at the end of a text file
and return the length of string appended"""
    if filename == "":
        with open("file_append.txt", "r", encoding="utf-8") as f:
            filename = "file_append.txt"
            pass

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
