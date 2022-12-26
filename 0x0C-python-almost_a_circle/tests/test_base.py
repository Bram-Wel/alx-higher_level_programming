#!/usr/bin/python3
"""This module describes a Test class."""


import unittest

from models.base import Base
from models.rectangle import Rectangle


class BaseTestCase(unittest.TestCase):
    """Tests the base class."""

    def setUp(self):
        """Create an instances of the base class."""
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base(17)
        self.object = None

    # @unittest.skip("")
    def tearDown(self):
        """Destroy instances after test."""
        del self.obj1
        del self.obj2
        del self.obj3

    def test_init(self):
        """Test initialisation of base object."""
        self.assertIsNotNone(self.obj1.id)
        self.assertIsNotNone(self.obj2.id)

        self.assertIsInstance(self.obj1.id, int)
        self.assertIsInstance(self.obj2.id, int)

        # Value of nb_instances when `id` is given ie: Base(12) or not; Base().
        self.assertEqual(self.obj1.id, self.obj2.id - 1)
        self.assertEqual(17, self.obj3.id)

        # `id` is a public attribute
        self.obj3.id = 20
        self.assertEqual(20, self.obj3.id)

        # __nb_instances is a private attribute
        with self.assertRaises(AttributeError):
            print(self.obj3.__nb_instances)

    def test_delete(self):
        """Test deletion of objects."""
        del self.obj1
        with self.assertRaises((NameError, AttributeError)):
            print(self.obj1)
        self.obj1 = Base()
        self.assertEqual(2, self.obj1.id)

    def test_jsonstring(self):
        """Test json string dump."""
        self.object = Rectangle(1, 2, 3, 4)
        self.assertTrue(type(self.object.to_json_string(None)) == str)
        dct = self.object.to_dictionary()
        self.assertTrue(type(self.object.to_json_string(dct)) == str)
