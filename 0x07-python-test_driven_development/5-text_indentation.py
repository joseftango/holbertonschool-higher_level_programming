#!/usr/bin/python3
"""__import__('5-text_indentation).text_indentation"""
def text_indentation(text):
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(f"{i}", end="")
            print("\n")
        else:
            print(f"{i}", end="")
