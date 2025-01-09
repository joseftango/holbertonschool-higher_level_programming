#!/usr/bin/python3
import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):

    def setUp(self):
        '''Reset the Base class's counter before each test.'''
        Base._Base__nb_objects = 0

    def test_Square_object_attributes(self):
        s = Square(1)
        self.assertIsNotNone(s)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s = Square(1, 2)
        self.assertIsNotNone(s)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)

        s = Square(1, 2, 3)
        self.assertIsNotNone(s)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        s = Square(1, 2, 3, 10)
        self.assertIsNotNone(s)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_Square_string_attributes(self):

        with self.assertRaises(TypeError) as context:
            s = Square('1')
        self.assertEqual(str(context.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as context:
            s = Square(1, '2')
        self.assertEqual(str(context.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as context:
            s = Square(1, 2, '3')
        self.assertEqual(str(context.exception), 'y must be an integer')

        s = Square(1, 2, 3, 4)
        self.assertIsNotNone(s)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_Square_negative_and_zero_attributes(self):

        with self.assertRaises(ValueError) as context:
            s = Square(-1)
        self.assertEqual(str(context.exception), 'width must be > 0')

        with self.assertRaises(ValueError) as context:
            s = Square(1, -2)
        self.assertEqual(str(context.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as context:
            s = Square(1, 2, -3)
        self.assertEqual(str(context.exception), 'y must be >= 0')

        with self.assertRaises(ValueError) as context:
            s = Square(0)
        self.assertEqual(str(context.exception), 'width must be > 0')

    def test_Square__str__instance_method(self):
        s = Square(5)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 5')

        s = Square(5, 3)
        self.assertEqual(str(s), '[Square] (2) 3/0 - 5')

        s = Square(5, 3, 7)
        self.assertEqual(str(s), '[Square] (3) 3/7 - 5')

        s = Square(5, 3, 7, 15)
        self.assertEqual(str(s), '[Square] (15) 3/7 - 5')

    def test_Square_to_dictionary_instance_method(self):
        
        s = Square(10)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 10, 'x': 0, 'y': 0})

        s = Square(10, 2)
        self.assertEqual(s.to_dictionary(), {'id': 2, 'size': 10, 'x': 2, 'y': 0})

        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(), {'id': 3, 'size': 10, 'x': 2, 'y': 1})

        s = Square(10, 2, 1, 60)
        self.assertEqual(s.to_dictionary(), {'id': 60, 'size': 10, 'x': 2, 'y': 1})


    def test_Square_update_instance_method(self):
        s = Square(5)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 5')

        s.update()
        self.assertEqual(str(s), '[Square] (1) 0/0 - 5')

        s.update(10)
        self.assertEqual(str(s), '[Square] (10) 0/0 - 5')

        s.update(1, 2)
        self.assertEqual(str(s), '[Square] (1) 0/0 - 2')

        s.update(1, 2, 3)
        self.assertEqual(str(s), '[Square] (1) 3/0 - 2')

        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (1) 3/4 - 2')

        s.update(**{ 'id': 89 })
        self.assertEqual(str(s), '[Square] (89) 3/4 - 2')

        s.update(**{ 'id': 89, 'width': 1 })
        self.assertEqual(str(s), '[Square] (89) 3/4 - 1')

        s.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(str(s), '[Square] (89) 3/4 - 1')
        
        s.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(str(s), '[Square] (89) 3/4 - 1')

        s.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 6 })
        self.assertEqual(str(s), '[Square] (89) 3/6 - 1')


    def test_Square_create_method(self):
        s = Square.create(**{ 'id': 89 })
        self.assertEqual(str(s), '[Square] (89) 0/0 - 10')

        s = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(str(s), '[Square] (89) 0/0 - 1')

        s = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(str(s), '[Square] (89) 2/0 - 1')

        s = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(str(s), '[Square] (89) 2/3 - 1')


    def test_save_to_file_method_case1(self):
        
        #Ensure the file does not exist before the test
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        Square.save_to_file(None)

        # Check if the file is created and contains "[]"
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        # Cleanup: Remove the file after test
        if os.path.exists("Square.json"):
            os.remove("Square.json")


    def test_save_to_file_method_case2(self):
        
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        Square.save_to_file([])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_save_to_file_method_case3(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        Square.save_to_file([Square(1)])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_Square_load_from_file(self):

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        res = Square.load_from_file()
        self.assertEqual(res, [])

        Square.save_to_file([Square(1)])

        res = Square.load_from_file()[0]
        self.assertEqual((res.id), 1)
        self.assertEqual((res.size), 1)
        self.assertEqual((res.x), 0)
        self.assertEqual((res.y), 0)

        if os.path.exists("Square.json"):
            os.remove("Square.json")
