"""applicate unittest to max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer
"""importing max_integer function from 6-max_integer"""


class test_max_integer(unittest.TestCase):
    """class named test_max_integer"""

    def test_regular_list(self):
        """function that tests a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 3, 4, 25]), 25)
        self.assertEqual(max_integer([111, 53, 46, 92]), 111)
        self.assertEqual(max_integer("hello"), "o")
        self.assertEqual(max_integer([60]), 60)
        self.assertEqual(max_integer(), None)

    def test_negative_list(self):
        """function that tests a list contain negtive values"""
        self.assertEqual(max_integer([-111, -53, -46, -92]), -46)
        self.assertEqual(max_integer([-1, -9, -6, 0]), 0)
        self.assertEqual(max_integer([2, -4, 6, -8, 0]), 6)
        self.assertEqual(max_integer([-11, -53, -46, -92]), -11)
        self.assertEqual(max_integer([-111, 1, -46, -92]), 1)

    def test_float_list(self):
        """function that tests a list contain float values"""
        self.assertEqual(max_integer([-11.1, -5.3, -4.6, -9.2]), -4.6)
        self.assertEqual(max_integer([5.5, 5.3, 4.6, 9.2]), 9.2)
        self.assertEqual(max_integer([5.5, -5.3, 4.6, -9.2]), 5.5)
        self.assertEqual(max_integer([0.2, -5.3, -4.6, -9.2]), 0.2)
        self.assertEqual(max_integer([-0.2, 0.3, -0.6, -9.2]), 0.3)
        self.assertEqual(max_integer((-0.2, 0.3, -0.6, -9.2)), 0.3)

    def test_excepted_errors_list(self):
        """function that tests errors"""
        self.assertRaises(TypeError, max_integer, ["-0.2", 0.3, -0.6, -9.2])
        self.assertRaises(TypeError, max_integer, [-0.6, "-9.2"])
        self.assertRaises(TypeError, max_integer, {-0.2, 0.3, -0.6, -9.2})
        self.assertRaises(TypeError, max_integer, [None, 0.3, -0.6, -9.2])
        self.assertRaises(TypeError, max_integer, [5, 0.3, None, -9.2])
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()
