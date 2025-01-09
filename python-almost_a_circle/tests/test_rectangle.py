#!/usr/bin/python3
import unittest
import os
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):

    def setUp(self):
        """Reset the Base class"s counter before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_object_attributes(self):
        r1 = Rectangle(10, 2)
        self.assertIsNotNone(r1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertIsNotNone(r2)
        self.assertEqual(r2.id, 2) 
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertIsNotNone(r3)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(r3)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsNotNone(r3)
        self.assertEqual(r3.id, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_rectangle_string_argument(self):

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsNotNone(r1)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        with self.assertRaises(TypeError) as context:
            r1 = Rectangle("1", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(1, "2")
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(1, 2, "3")
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(1, 2, 3, "4")
        self.assertEqual(str(context.exception), "y must be an integer")
        
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(-1, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(1, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(0, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(1, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(1, 2, -3)
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_rectangle_area_method(self):
            r1 = Rectangle(10, 5, 0, 0, 30)
            self.assertEqual(r1.area(), 50)

            r1 = Rectangle(4, 2, 0, 0, 30)
            self.assertEqual(r1.area(), 8)

            r1 = Rectangle(5, 5, 0, 0, 30)
            self.assertEqual(r1.area(), 25)

            r1 = Rectangle(5, 8, 0, 0, 30)
            self.assertEqual(r1.area(), 40)

    def test_Rectangle__str__method(self):
        r1 = Rectangle(10, 5, 0, 0, 30)
        self.assertEqual(str(r1), "[Rectangle] (30) 0/0 - 10/5")

        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

        r1 = Rectangle(5, 10, 0, 0, 0)
        self.assertEqual(str(r1), "[Rectangle] (0) 0/0 - 5/10")

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_instance_method_case1(self, mock_stdout):
        rect = Rectangle(4, 3, 0, 0, 30)

        rect.display()

        expected_output = "####\n" + \
                          "####\n" + \
                          "####\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_instance_method_case2(self, mock_stdout):
        rect = Rectangle(5, 5, 0, 0, 30)

        rect.display()

        expected_output = "#####\n" + \
                          "#####\n" + \
                          "#####\n" + \
                          "#####\n" + \
                          "#####\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_instance_method_case3(self, mock_stdout):
        rect = Rectangle(5, 5, 3, 0, 30)

        rect.display()

        expected_output = "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_instance_method_case3(self, mock_stdout):
        rect = Rectangle(5, 5, 3, 0, 30)

        rect.display()

        expected_output = "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_instance_method_case3(self, mock_stdout):
        rect = Rectangle(5, 5, 3, 2, 30)

        rect.display()

        expected_output = "\n" \
                          "\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n" + \
                          "   #####\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_Rectangle_method_to_dictionary(self):

        r1 = Rectangle(10, 2, 1, 9, 30)
        res = {"x": 1, "y": 9, "id": 30, "height": 2, "width": 10}
        self.assertEqual(r1.to_dictionary(), res)

        r1 = Rectangle(4, 6, 5, 3, 30)
        res = {"x": 5, "y": 3, "id": 30, "height": 6, "width": 4}
        self.assertEqual(r1.to_dictionary(), res)

    def test_Rectangle_update_method(self):

        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 1)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 1/10")

        r1.update(89, 1, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 1/2")

        r1.update(89, 1, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/10 - 1/2")

        r1.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 1/2")

        r2 = Rectangle(10, 10, 10, 10, 10)
        r2.update(**{ "id": 89 })
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 10/10")

        r2.update(**{ "id": 50, "width": 1 })
        self.assertEqual(str(r2), "[Rectangle] (50) 10/10 - 1/10")
        
        r2.update(**{ "id": 89, "width": 1, "height": 2 })
        self.assertEqual(str(r2), "[Rectangle] (89) 10/10 - 1/2")

        r2.update(**{ "id": 70, "width": 1, "height": 2, "x": 3 })
        self.assertEqual(str(r2), "[Rectangle] (70) 3/10 - 1/2")

        r2.update(**{ "id": 89, "width": 1, "height": 2, "x": 3, "y": 4 })
        self.assertEqual(str(r2), "[Rectangle] (89) 3/4 - 1/2")

    def test_Rectangle_create_method(self):

        r1 = Rectangle(5, 5, 5, 5, 3)
        obj = r1.create(**{ "id": 89 })
        self.assertEqual(str(obj), "[Rectangle] (89) 0/0 - 10/10")

        obj = Rectangle.create(**{ "id": 89, "width": 1 })
        self.assertEqual(str(obj), "[Rectangle] (89) 0/0 - 1/10")

        obj = Rectangle.create(**{ "id": 89, "width": 1, "height": 2 })
        self.assertEqual(str(obj), "[Rectangle] (89) 0/0 - 1/2")

        obj = Rectangle.create(**{ "id": 89, "width": 1, "height": 2, "x": 3 })
        self.assertEqual(str(obj), "[Rectangle] (89) 3/0 - 1/2")

        obj = Rectangle.create(**{ "id": 89, "width": 1, "height": 2, "x": 3, "y": 4 })
        self.assertEqual(str(obj), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file_method_case1(self):
        
        #Ensure the file does not exist before the test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file(None)

        # Check if the file is created and contains "[]"
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        # Cleanup: Remove the file after test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_method_case2(self):
        
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file([])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_method_case3(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        Rectangle.save_to_file([Rectangle(1, 2)])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"x": 0, "y": 0, "id": 1, "height": 2, "width": 1}]')

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


    def test_Rectangle_load_from_file(self):

            res = Rectangle.load_from_file()
            self.assertEqual(res, [])
        
            Rectangle.save_to_file([Rectangle(1, 2)])
            res = Rectangle.load_from_file()[0]
            self.assertEqual((res.id), 1)
            self.assertEqual((res.width), 1)
            self.assertEqual((res.height), 2)
            self.assertEqual((res.x), 0)
            self.assertEqual((res.y), 0)

            Rectangle.save_to_file([Rectangle(5, 3, 2, 2, 80), Rectangle(15, 13, 22, 22, 90)])
            res = Rectangle.load_from_file()[0]
            self.assertEqual((res.id), 80)
            self.assertEqual((res.width), 5)
            self.assertEqual((res.height), 3)
            self.assertEqual((res.x), 2)
            self.assertEqual((res.y), 2)

            res = Rectangle.load_from_file()[1]
            self.assertEqual((res.id), 90)
            self.assertEqual((res.width), 15)
            self.assertEqual((res.height), 13)
            self.assertEqual((res.x), 22)
            self.assertEqual((res.y), 22)
