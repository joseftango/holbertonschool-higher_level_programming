#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

argv_num = len(argv) - 1

if (argv_num == 0):
    print(f"{argv_num} arguments.")

elif (argv_num == 1):
    print(f"{argv_num} argument:\n{argv_num}: {argv[1]}")

else:
    print(f"{argv_num} argument:")
    for i in range(1, argv_num + 1):
        print(f"{i}: {argv[i]}")
