#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
        number = number % 10
        return number + number * 10
    else:
        number = number % 10
        print(number, end="")
