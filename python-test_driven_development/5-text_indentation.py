#!/usr/bin/python3
"""5-def text_indentation module"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters .?:"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i in range(len(text)):
        if text[i] in '.?:':
            print(text[i], end='')
            print()
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i = i + 2
                continue
            i = i + 1
        else:
            print(text[i], end='')
            i = i + 1
