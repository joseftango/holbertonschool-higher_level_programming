#!/usr/bin/python3
def fizzbuzz():
    n = 1
    while n <= 100:
        if n % 3 == 0:
            print('Fizz', end=' ')
        elif n % 5 == 0:
            print('Buzz', end=' ')
        elif n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print('{}'.format(n), end=' ')
        n += 1
