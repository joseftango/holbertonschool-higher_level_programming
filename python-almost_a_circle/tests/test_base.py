#!/usr/bin/python3
import unittest
from models.base import Base
from json import dumps


class Test_Base(unittest.TestCase):
    def setUp(self):
        '''Reset the Base class's counter before each test.'''
        Base._Base__nb_objects = 0

    def test_Base_auto_id_assignment(self):
        b1 = Base()
        self.assertIsNotNone(b1.id)
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertIsNotNone(b2.id)
        self.assertEqual(b2.id, 2)

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

    def test_saving_id_passed_as_argument(self):
        b1 = Base(50)
        self.assertEqual(b1.id, 50)
        b1 = Base(-10)
        self.assertEqual(b1.id, -10)
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

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

    def test_Base_method_to_json_string(self):
        res = Base.to_json_string(None)
        self.assertEqual(res, '[]')

        res = Base.to_json_string([])
        self.assertEqual(res, '[]')

        res = None
        res = Base.to_json_string([{'id': 1}])
        self.assertIsNotNone(res)
        self.assertEqual(res, '[{"id": 1}]')

        res = None
        res = Base.to_json_string([{'id': 1, 'name': 'Jo'}, {'id': 2, 'name': 'Andrew'}, {'id': 3, 'name': 'Paulo'}])
        self.assertIsNotNone(res)
        self.assertEqual(res, dumps([{'id': 1, 'name': 'Jo'}, {'id': 2, 'name': 'Andrew'}, {'id': 3, 'name': 'Paulo'}]))

        res = None
        res = Base.to_json_string([{'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}])
        self.assertIsNotNone(res)
        self.assertEqual(res, dumps([{'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}]))

    def test_Base_method_from_json_string(self):

        res = None
        res = Base.from_json_string(None)
        self.assertIsNotNone(res)
        self.assertEqual(res, [])

        res = None
        res = Base.from_json_string('[]')
        self.assertIsNotNone(res)
        self.assertEqual(res, [])

        res = None
        res = Base.from_json_string('[{"id": 1}]')
        self.assertIsNotNone(res)
        self.assertEqual(res, [{"id": 1}])

        res = None
        res = Base.from_json_string('[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')
        self.assertIsNotNone(res)
        self.assertEqual(res, [{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}])

        res = None
        res = Base.from_json_string('[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')
        self.assertIsNotNone(res)
        self.assertEqual(res, [{'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}])
