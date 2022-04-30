#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * (-1)
    justdigit = number % 10
    print(f"{justdigit}", end="")
    return justdigit
