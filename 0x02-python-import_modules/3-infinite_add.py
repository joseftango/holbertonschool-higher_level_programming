#!/usr/bin/python3

if __name__ == '__main__':
    import sys
add = 0
if len(sys.argv) < 2:
    print(f"{0}")
else:
    for i in sys.argv[1:]:
        add += int(i)
    print(f"{add}")
