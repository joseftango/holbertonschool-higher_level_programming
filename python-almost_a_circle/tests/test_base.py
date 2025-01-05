#!/usr/bin/python3
"""Unittest for Base.py
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseModule(unittest.TestCase):
    """TestBaseModule class
    this class is to test the Base class from models/base.py
    """
    def test_base_id_empty(self):
        """test_base_id_empty method
        this method tests if the function properly works
        with None and empty
        """
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

    def test_base_to_json_string(self):
        """test_base_to_json_string method
        this method tests if the function properly works as expected
        """
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_base_create(self):
        """test_base_create method
        Tests the base class create classmethod without kwarg
        """
        with self.assertRaises(TypeError) as err:
            warn = Rectangle.create('string')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were\
 given", str(err.exception))

    def test_base_load_from_file(self):
        """test_base_load_from_file method
        Tests the base class load_from_file classmethod without kwarg
        """
        paths = ["Base.json", "Rectangle.json", "Square.json"]
        for path in paths:
            if os.path.exists(path):
                os.remove(path)

        empty_square = Square.load_from_file()
        self.assertEqual(empty_square, [])

        empty_rect = Rectangle.load_from_file()
        self.assertEqual(empty_rect, [])

        with self.assertRaises(TypeError) as err:
            Rectangle.load_from_file('string')

        self.assertEqual(
            "load_from_file() takes 1 positional argument but 2 were\
 given", str(err.exception))
