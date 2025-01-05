#!/usr/bin/python3
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):

    def test_base_id_auto_assignment(self):
        '''Test of Base() for assigning automatically an ID exists'''
        bTest = Base()
        self.assertEqual(bTest.id, 1)
        bTest = Base(None)
        self.assertEqual(bTest.id, 2)

    def test_base_id_positive(self):
        """test_base_id_positive method
        this method tests if the function properly works
        with positive numbers
        """
        b = Base(68)
        self.assertEqual(b.id, 68)

        b = Base(345)
        self.assertEqual(b.id, 345)

    def test_base_id_negative(self):
        """test_base_id_positive method
        this method tests if the function properly works
        with negative numbers
        """
        b = Base(-44)
        self.assertEqual(b.id, -44)
        b = Base(-32)
        self.assertEqual(b.id, -32)
