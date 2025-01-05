#!/usr/bin/python3
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):

    def test_base_id_auto_assignment(self):
        b1 = Base()

        self.assertIsNotNone(b1.id)
        self.assertEqual(b1.id, 1)

        b2 = Base()

        self.assertIsNotNone(b2.id)
        self.assertEqual(b2.id, 2)

        b3 = Base()

        self.assertIsNotNone(b3.id)
        self.assertEqual(b3.id, 3)

    def test_base_saving_id_passed(self):
        b1 = Base(20)
        self.assertEqual(b1.id, 20)

        b2 = Base(50)
        self.assertEqual(b2.id, 50)

