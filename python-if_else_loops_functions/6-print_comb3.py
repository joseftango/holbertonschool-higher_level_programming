#!/usr/bin/python3
for x in range(0, 120):
    if (x == 89):
        print(f"{x:02d}")
        break
    if (x / 10) < (x % 10):
        print(f"{x:02d}", end=", ")
