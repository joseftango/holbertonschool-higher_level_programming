#!/usr/bin/python3

"""
a = "banana"
b = "banana"

print(a == b)
print(a is b)
'''
This tells us that both a and b refer to the same object. Since strings are immutable, Python optimizes resources by
making two names that refer to the same string value refer to the same object.
This is not the case with lists:
'''
"""

'''a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
'''

'''a = [1, 2, 3]
b = a
print(a is b)

# Because the same list has two different names, a and b, we say that it is aliased. Changes made with one alias affect the other:

b[0] = 5
print(a)
'''

'''a = [1, 2, 3]
b = a[:]
print(b)

b[0] = 5
print(a)
print(b)
'''

'''numbers = [1, 2, 3, 4, 5]
for index, value in enumerate(numbers):
	print(index, value)
'''

'''
for index, value in enumerate(['banana', 'apple', 'pear', 'quince']):
	print(index, value)
'''

'''li = [1, 2, 3]
li += [4]
print(li)
li += [5]
print(li)
'''

'''def double_stuff(a_list):
    new_list = []
    for value in a_list:
        new_list += [2 * value]
    return new_list

things = [2, 5, 'Spam', 9.5]
print(double_stuff(things))
print(things)

things = double_stuff(things)
print(things)
'''

'''
x = 5.0
print(id(x))
x += 7.0
print(id(x))

s = 'foo'
print(id(s))
s += 'bar'
print(id(s))

li = [1, 2, 3]
print(id(li))
li += [4, 5]
print(id(li))
'''

'''x = 'foo'
y = x
print(id(x))
print(id(y))

print(x) # foo
y += 'bar'
print(x) # foo
print(id(x))
print(id(y))
'''

'''x = [1, 2, 3]
y = x
print(x) # [1, 2, 3]
y += [3, 2, 1]
print(x) # [1, 2, 3, 3, 2, 1]
print(id(x))
print(id(y))
'''


'''def func(val):
    val += 'bar'
    print(id(val))

x = 'foo'
print(id(x)) # foo
func(x)
print(id(x)) # foo
'''

'''def func(val):
    val += [3, 2, 1]

x = [1, 2, 3]
print(id(x))# [1, 2, 3]
func(x)
print(id(x))# [1, 2, 3, 3, 2, 1]
'''

'''l = [1, 2, 3]
print(id(l))
l += [4, 5]                       
print(l)
print(id(l))

t = (1, 2, 3)
print(id(t))
t += (4, 5)                       
print(t)
print(id(t))
'''

s = {1, 2, 3}
s1 = {1, 2, 3}
print(id(s))
print(id(s1))
