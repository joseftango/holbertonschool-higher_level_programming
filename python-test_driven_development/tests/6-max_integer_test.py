#!/usr/bin/python3
"""6-max_integer_test module that test max_integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
	"""testing max_integer function in a list"""
	def test_list_of_positive_integers(self):
		self.assertEqual(max_integer([1, 2, 3, 4]), 4)
		self.assertEqual(max_integer([4, 3, 2, 1]), 4)
		self.assertEqual(max_integer([50, 30, 60, 10]), 60)

	def test_list_of_negative_integers(self):
		self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
		self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
		self.assertEqual(max_integer([-50, -30, -60, -10]), -10)

	def test_list_of_both_negative_and_positive_ints(self):
		self.assertEqual(max_integer([-50, 30, -60, 10]), 30)
		self.assertEqual(max_integer([-5, 7, -60, 5]), 7)
		self.assertEqual(max_integer([10, -30, 0, 10, -54, 41, 12, -33]), 41)

	def test_empty_list_and_args(self):
		self.assertEqual(max_integer([]), None)
		self.assertEqual(max_integer(), None)
