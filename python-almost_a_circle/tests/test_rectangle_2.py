#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):

    def test_rectangle_object_existance_and_id(self):
        r1 = Rectangle(10, 2)

        self.assertIsNotNone(r1)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)

        self.assertIsNotNone(r2)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertIsNotNone(r3)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(10, 2, 0, 0, {12, 13, 15})
        self.assertEqual(r4.id, {12, 13, 15})

        r4 = Rectangle(10, 2, 0, 0, {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(r4.id, {'a': 1, 'b': 2, 'c': 3})

        r4 = Rectangle(10, 2, 0, 0, [1, 2, 3])
        self.assertEqual(r4.id, [1, 2, 3])

        r4 = Rectangle(10, 2, 0, 0, 'my_id')
        self.assertEqual(r4.id, 'my_id')

        r4 = Rectangle(10, 2, 0, 0, True)
        self.assertEqual(r4.id, True)

        r4 = Rectangle(10, 2, 0, 0, {1, 2, 3})
        self.assertEqual(r4.id, {1, 2, 3})

        r4 = Rectangle(10, 2, 0, 0, 55.021)
        self.assertEqual(r4.id, 55.021)

    def test_rectangle_negative_id(self):
        r1 = Rectangle(0, 0, 0, 0, -1)
        self.assertEqual(r1.id, -1)
        r2 = Rectangle(0, 0, 0, 0, -10)
        self.assertEqual(r2.id, -10)
        r3 = Rectangle(0, 0, 0, 0, -55)
        self.assertEqual(r3.id, -55)

    def test_rectangle_id_different_datatypes(self):
        b1 = Rectangle(0, 0, 0, 0, '-111')
        self.assertEqual(b1.id, '-111')

        b2 = Rectangle(0, 0, 0, 0, [1, 2, 3])
        self.assertEqual(b2.id, [1, 2, 3])

        b4 = Rectangle(0, 0, 0, 0, {'name': 'Jon', 'age': 20})
        self.assertEqual(b4.id, {'name': 'Jon', 'age': 20})

        b5 = Rectangle(0, 0, 0, 0, True)
        self.assertEqual(b5.id, True)

        b6 = Rectangle(0, 0, 0, 0, 'Python')
        self.assertEqual(b6.id, 'Python')

        b7 = Rectangle(0, 0, 0, 0, {1, 2, 3})
        self.assertEqual(b7.id, {1, 2, 3})

        b8 = Rectangle(0, 0, 0, 0, (1, 2, 3))
        self.assertEqual(b8.id, (1, 2, 3))

    def test_width_and_height(self):
        r_one = Rectangle(10, 20, 0, 0, 50)
        self.assertEqual(r_one.width, 10)
        self.assertEqual(r_one.height, 20)

        r_one = Rectangle(0, 0, 0, 0, 50)
        self.assertEqual(r_one.width, 0)
        self.assertEqual(r_one.height, 0)

        r_two = Rectangle(-10, -20, 0, 0, 50)
        self.assertEqual(r_two.width, -10)
        self.assertEqual(r_two.height, -20)

        r_two = Rectangle(None, None, 0, 0, 50)
        self.assertEqual(r_two.width, None)
        self.assertEqual(r_two.height, None)

        r_two = Rectangle(55.648, 78.654, 0, 0, 50)
        self.assertEqual(r_two.width, 55.648)
        self.assertEqual(r_two.height, 78.654)

        r_two = Rectangle('Hello', 'Micheal', 0, 0, 50)
        self.assertEqual(r_two.width, 'Hello')
        self.assertEqual(r_two.height, 'Micheal')

        r_two = Rectangle([1, 2], [2, 3], 0, 0, 50)
        self.assertEqual(r_two.width, [1, 2])
        self.assertEqual(r_two.height, [2, 3])

        r_two = Rectangle(True, False, 0, 0, 50)
        self.assertEqual(r_two.width, True)
        self.assertEqual(r_two.height, False)

        r_two = Rectangle({'name': 'Jon', 'age': 20}, {'name': 'Jon', 'age': 20}, 0, 0, 50)
        self.assertEqual(r_two.width, {'name': 'Jon', 'age': 20})
        self.assertEqual(r_two.height, {'name': 'Jon', 'age': 20})

        with self.assertRaises(TypeError) as e:
            r_two = Rectangle()
            self.assertEqual(str(e.exception), "Rectangle.__init__() missing 2 required positional arguments: 'width' and 'height'")

        with self.assertRaises(TypeError) as e:
            r_two = Rectangle(5, )
            self.assertEqual(str(e.exception), "Rectangle.__init__() missing 1 required positional argument: 'height'")

    def test_x_and_y(self):
        r_ten = Rectangle(8, 12, 5, 10, 5)
        self.assertEqual(r_ten.x, 5)
        self.assertEqual(r_ten.y, 10)

        r_ten = Rectangle(8, 12)
        self.assertEqual(r_ten.x, 0)
        self.assertEqual(r_ten.y, 0)

        r_ten = Rectangle(8, 12, -5, -10)
        self.assertEqual(r_ten.x, -5)
        self.assertEqual(r_ten.y, -10)

        r_ten = Rectangle(8, 12, 'Hello', 'Mike')
        self.assertEqual(r_ten.x, 'Hello')
        self.assertEqual(r_ten.y, 'Mike')

        r_ten = Rectangle(8, 12, {'Hello', 'Mike', 1, 2, 3}, {1, 2, 3})
        self.assertEqual(r_ten.x, {'Hello', 'Mike', 1, 2, 3})
        self.assertEqual(r_ten.y, {1, 2, 3})

        r_ten = Rectangle(8, 12, [1, 2, 3], [4, 5, 6])
        self.assertEqual(r_ten.x, [1, 2, 3])
        self.assertEqual(r_ten.y, [4, 5, 6])

        r_ten = Rectangle(8, 12, (1, 2, 3), (4, 5, 6))
        self.assertEqual(r_ten.x, (1, 2, 3))
        self.assertEqual(r_ten.y, (4, 5, 6))

        r_ten = Rectangle(8, 12, None, None)
        self.assertEqual(r_ten.x, None)
        self.assertEqual(r_ten.y, None)

        r_ten = Rectangle(8, 12, True, False)
        self.assertEqual(r_ten.x, True)
        self.assertEqual(r_ten.y, False)

        r_ten = Rectangle(8, 12, 55.55, 88.88)
        self.assertEqual(r_ten.x, 55.55)
        self.assertEqual(r_ten.y, 88.88)

