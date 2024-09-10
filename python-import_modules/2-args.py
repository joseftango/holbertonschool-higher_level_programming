#!/usr/bin/python3
from sys import argv
num_of_args = len(argv[1:])
args = argv[1:]

if __name__ == '__main__':
	if num_of_args > 0:
		print('{} arguments:'.format(num_of_args))
		for i in range(num_of_args):
			print('{}: {}'.format(i + 1, args[i]))
	else:
		print('0 arguments.')
