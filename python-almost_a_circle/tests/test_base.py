#!/usr/bin/python3
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):

    def test_base_object_existance_and_id(self):
        b10 = Base()

        self.assertIsNotNone(b10)
        self.assertEqual(b10.id, 1)

        b11 = Base()

        self.assertIsNotNone(b11)
        self.assertEqual(b11.id, 2)

        b12 = Base()

        self.assertIsNotNone(b12)
        self.assertEqual(b12.id, 3)

        b13 = Base(12)

        self.assertIsNotNone(b13)
        self.assertEqual(b13.id, 12)

        b14 = Base()

        self.assertIsNotNone(b14)
        self.assertEqual(b14.id, 4)

        b15 = Base(None)
        self.assertEqual(b15.id, 5)

    def test_base_negative_id(self):
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)
        b1 = Base(-10)
        self.assertEqual(b1.id, -10)
        b1 = Base(-55)
        self.assertEqual(b1.id, -55)

    def test_base_id_different_datatypes(self):
        b1 = Base('-111')
        self.assertEqual(b1.id, '-111')

        b2 = Base([1, 2, 3])
        self.assertEqual(b2.id, [1, 2, 3])

        b4 = Base({'name': 'Jon', 'age': 20})
        self.assertEqual(b4.id, {'name': 'Jon', 'age': 20})

        b5 = Base(True)
        self.assertEqual(b5.id, True)

        b6 = Base('Python')
        self.assertEqual(b6.id, 'Python')

        b7 = Base({1, 2, 3})
        self.assertEqual(b7.id, {1, 2, 3})

        b8 = Base((1, 2, 3))
        self.assertEqual(b8.id, (1, 2, 3))

        b8 = Base(55.215)
        self.assertEqual(b8.id, 55.215)
