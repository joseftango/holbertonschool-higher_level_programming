#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_normal_integer(self):
        """testing unsigned integer in list"""
        max_integer([1,10,5,6,3])
        self.assertEqual(10)

    def test_negative_integer(self):
        """testing negative integer in list"""
        max_integer([-1,-10,-5,0])
        self.assertEqual(0)

    def test_empty_list(self):
        """testing empty list"""
        max_integer([])
        self.assertEqual(None)

    def test_single_num(self):
        """testing single integer in list"""
        max_integer([50])
        self.assertEqual(50)
