#!/usr/bin/python3

if __name__ == '__main__':
	import hidden_4

names = dir(hidden_4)

for item in names:
	if item[0] != '_' and item[1] != '_':
		print(f"item")
