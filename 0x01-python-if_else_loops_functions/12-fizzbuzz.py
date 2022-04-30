#!/usr/bin/python3
def fizzbuzz():
    i = 1
    for i in range(i, 101):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=" ")
        else:
            print(i, end=" ")
