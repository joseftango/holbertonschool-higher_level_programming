#!/usr/bin/python3
'''0-read_file module'''


def write_file(filename="", text=""):
    '''function that writes a string to a text file
    (UTF8) and returns the number of characters'''
    with open(filename, 'w', encoding='UTF-8') as f:
        length = f.write(text)
    return length
