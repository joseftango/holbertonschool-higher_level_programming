#!/usr/bin/python3

for j in range(90, 64, -1):
	if j % 2 == 0:
		print('{}'.format(chr(j)), end='')
	else:
		j += 32
		print('{}'.format(chr(j)), end='')

# for i in range(25, -1, -1):
# 	if i % 2 == 0:
# 		print('{}'.format(chr(ord('a') + i)), end='')
# 	else:
# 		print('{}'.format(chr(ord('A') + i)), end='')
