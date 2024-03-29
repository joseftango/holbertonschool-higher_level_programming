#!/usr/bin/python3
"""3-say_my_name = __import__("3-say_my_name").__doc__)"""


def say_my_name(first_name, last_name=""):
    """function that print a name"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
