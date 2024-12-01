#!/usr/bin/python3

li = ['cat', 'dog', 'hamster', 'cow']
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'strawberry']

# li.append('mouse') # add new element at the end of the list
# print(li)
# li[len(li):] = ['goat'] # same thing using slice
# print(li)

# li.extend(['pig', 'hourse', 'bird'])
# print(li)

# li.insert(2, 'mouse')
# print(li)
# li.insert(len(li), 'crocodile') # equivalent to li.append('crocodile')
# print(li)

# li.remove('cat')
# print(li)

# li.pop(0)
# print(li)
# li.pop()
# print(li)

# li.clear() # equivalent to del li[:]
# print(li)

# print(fruits.index('banana', 4, 7))
# print(fruits.index('kiwi'))

# print(fruits.count('banana'))
# print(fruits.count('kiwi'))

# fruits.sort()
# print(fruits)
# li.insert(0, 'zebra')
# print(sorted(li))
# print(li)

# li.reverse()
# print(li)

# li2 = li.copy() # same as li[:]
# print(id(li2), id(li))


# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))

# print(fruits.count('tangerine'))

# print(fruits.index('banana'))

# print(fruits.index('banana', 4))  # Find next banana starting at position 4

# fruits.reverse()
# print(fruits)
# fruits.append('grape')
# print(fruits)

# fruits.sort()
# print(fruits)

# print(fruits.pop())


# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# print(queue.popleft())                 # The first to arrive now leaves
# print(queue.popleft())                # The second to arrive now leaves
# print(queue)                           # Remaining queue in order of arrival

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# saqures = [x ** 2 for x in range(10)]
# print(saqures)

# squares = list(map(lambda x: x**2, range(10)))
# print(saqures)


# list1 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

# print(list1)

# list2 = []

# for x in [1, 2, 3]:
# 	for y in [3, 1, 4]:
# 		if x != y:
# 		    list2.append((x, y))

# print(list2)


# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# [x*2 for x in vec]
# [-8, -4, 0, 4, 8]
# # filter the list to exclude negative numbers
# [x for x in vec if x >= 0]
# [0, 2, 4]
# # apply a function to all the elements
# [abs(x) for x in vec]

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']
# # create a list of 2-tuples like (number, square)
# [(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# #the tuple must be parenthesized, otherwise an error is raised
# must [x, x**2 for x in range(6)]

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# new = [num for sub_li in vec for num in sub_li]
# print(new)

# from math import pi
# li = [str(round(pi, i)) for i in range(1, 6)]
# print(li)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# print([[row[i] for row in matrix] for i in range(4)])

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)

# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# print(transposed)

# print(*matrix) 
# the * operator unpacj matrix to become : [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
# print(list(zip(*matrix)))

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# del a
# print(a) # NameError: name 'a' is not defined


# t = 12345, 54321, 'hello!'
# t[0]

# print(t)

# # Tuples may be nested:
# u = t, (1, 2, 3, 4, 5)
# print(u)
# # Tuples are immutable:
# # t[0] = 88888
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: 'tuple' object does not support item assignment
# # but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])
# print(v)

# empty = ()
# singleton = 'hello',    # <-- note trailing comma
# print(len(empty))

# print(len(singleton))

# print(singleton)


# t = 12345, 54321, 'hello!'

# x, y, z = t

# print(x, z)


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a, b)

print(a)                                  # unique letters in a
print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
