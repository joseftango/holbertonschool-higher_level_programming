#!/usr/bin/python3
"""5-text_indentation = __import__(5-text_indentation).__doc__"""


def text_indentation(text):
	"""
	>>> text_indentation(""Lorem ipsum dolor sit amet: consectetur adipiscing elit.\
	...	Quonam modo?first solve the problem:then write.the code?"")
	Lorem ipsum dolor sit amet:
	<BLANKLINE>
	consectetur adipiscing elit.
	<BLANKLINE>
	Quonam modo?
	<BLANKLINE>
	first solve the problem:
	<BLANKLINE>
	then write.
	<BLANKLINE>
	the code?
	<BLANKLINE>

	>>> text_indentation(":?.")
	:
	<BLANKLINE>
	?
	<BLANKLINE>
	.
	<BLANKLINE>
	>>> text_indentation("10:15?20.")
	10:
	<BLANKLINE>
	15?
	<BLANKLINE>
	20.
	<BLANKLINE>
	>>> text_indentation("")
	>>> text_indentation(55555)
	Traceback (most recent call last):
		...
	TypeError: text must be a string

	>>> text_indentation(None)
	Traceback (most recent call last):
		...
	TypeError: text must be a string

	>>> text_indentation()
	Traceback (most recent call last):
		...
	TypeError: text_indentation() missing 1 required positional argument: 'text'
	"""
	if type(text) is not str:
		raise TypeError("text must be a string")
	for c in text:
		print(c, end="")
		if c in [".","?", ":"]:
			print("\n")
	"""function that prints a text with
	2 new lines after a specific character"""
	