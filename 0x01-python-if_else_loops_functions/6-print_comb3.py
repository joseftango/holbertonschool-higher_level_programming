#!/usr/bin/python3
for x in range(0, 100):
    if x == 99:
        print(f"{x}")
    if (x / 10) < (x % 10):
        print(f"{x:02d}", end=", ")
