#!/usr/bin/python3
"""5-text_indentation = __import__(5-text_indentation).__doc__"""


def text_indentation(text):
    """function that prints a text with
    2 new lines after a specific character"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        print(c, end="")
        if c in [".", "?", ":"]:
            print("\n")
