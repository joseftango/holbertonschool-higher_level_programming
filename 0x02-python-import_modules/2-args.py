#!/usr/bin/python3
import sys
count = 1
if(len(sys.argv) == 1):
    print("0 arguments.")
else:
    num = len(sys.argv[1:])
    print(f"{num} arguments:")
    for arg in sys.argv[1:]:
        print(f"{count}: {arg}")
        count = count + 1
