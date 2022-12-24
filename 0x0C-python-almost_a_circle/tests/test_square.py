#!/usr/bin/python3
"""Test module for square class."""


import unittest

from models.square import Square

TestCase = unittest.TestCase

class SquareTestCase(TestCase):
    """Test class for the square package.

    Args:
        TestCase: Unittest test class.
    """

    def setUp(self):
        """Make square instances."""
        self.obj1 = Square(5)
        self.obj2 = Square(5, 2)
        self.obj3 = Square(5, 2, 3)
        self.obj4 = Square(5, 2, 3, 24)


    def teardown(self):
        """Destroy square instances."""
        del self.obj1
        del self.obj2
        del self.obj3
        del self.obj4
        del self.obj5

    def test_init(self):
        """Test initialisation."""
        with self.assertRaises((TypeError, ValueError)):
            self.object = Square()
            self.object = Square(1, 2, 3, 4, 5)
            self.object = Square("string")
            self.object = Square("str", 16)
            self.object = Square(90, "1000")
            self.object = Square(1, 2, "3")
            self.object = Square(1, 2, 3, "4")
            self.object = Square(-1, 2)
            self.object = Square(2, -1)
            self.object = Square(2, 0)
            self.object = Square(0, 3)
            self.object = Square(1, 2, -3)
            self.object = Square(1, 2, 3, -4)

        self.assertIsNotNone(self.obj1.id)
        self.assertIsNotNone(self.obj2.id)
        self.assertIsNotNone(self.obj3.id)
        self.assertEqual(self.obj4.id, 24)
        self.assertEqual(self.obj2.size, 5)
        self.assertEqual(self.obj3.x, 2)
        self.assertEqual(self.obj3.y, 3)
