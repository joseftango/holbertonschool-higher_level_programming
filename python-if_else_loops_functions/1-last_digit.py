#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_degit = number * (-1) % 10
    last_degit = last_degit * (-1)
else:
    last_degit = number % 10

if last_degit > 5:
    print(f'Last digit of {number} is {last_degit} and is greater than 5')
elif number % 10 < 0:
    print(f'Last digit of {number} is {last_degit} and is 0')
elif last_degit < 6 and last_degit != 0:
    print(f'Last digit of {number} is {last_degit} \
and is less than 6 and not 0')
