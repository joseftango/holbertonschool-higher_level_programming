#!/usr/bin/python3
def uppercase(str):
    word = ""
    for i in str:
        if ord(i) <= 122 and ord(i) >= 97:
            word += chr(ord(i) - 32)
        else:
            word += i
    print(f"{word}")
