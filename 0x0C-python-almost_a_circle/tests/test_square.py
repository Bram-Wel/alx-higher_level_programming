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

    def test_gettersandsetters(self):
        """Test getters & setters."""
        self.obj1.x = 6
        self.obj1.y = 7
        self.assertEqual(self.obj1.x, 6)
        self.assertEqual(self.obj1.y, 7)
        self.obj2.size = 60
        self.obj3.id = 101
        self.assertEqual(self.obj2.size, 60)
        # self.assertEqual(self.obj2.height, 75)
        self.assertEqual(self.obj3.id, 101)
        setattr(self.obj1, 'size', 12)
        size = getattr(self.obj1, 'size')
        self.assertEqual(size, 12)
        setattr(self.obj1, 'x', 50)
        x = getattr(self.obj1, 'x')
        self.assertEqual(x, 50)
        setattr(self.obj2, 'y', 100)
        y = getattr(self.obj2, 'y')
        self.assertEqual(y, 100)
        setattr(self.obj3, 'id', 1001)
        id = getattr(self.obj3, 'id')
        self.assertEqual(id, 1001)
        # setattr(self.obj3, 'id', None)
        # id = getattr(self.obj3, 'id')
        # self.assertIsNone(id)
        setattr(self.obj4, 'test', "Test adding attribute")
        self.assertIn('test', dir(self.obj4), msg="test attribute not added")

        with self.assertRaises((ValueError, TypeError)):
            setattr(self.obj1, 'x', "String")
            setattr(self.obj2, 'y', ["lists", 12])
            setattr(self.obj3, 'size', ())
            setattr(self.obj1, 'size', 16.04)
            setattr(self.obj1, 'size', 0)
            setattr(self.obj2, 'size', -12)
            setattr(self.obj2, 'x', -1)
            setattr(self.obj3, 'y', -100)
            self.obj2.size = None
            self.assertIsNone(self.obj2.size)
            self.obj1.x = None
            self.assertIsNone(self.obj1.x)
            self.obj3.y = None
            self.assertIsNone(self.obj3.y)
            # self.obj4.id = None
            # self.assertIsNone(self.obj4.id)


        setattr(self.obj1, 'x', 0)
        self.assertEqual(0, self.obj1.x)
        setattr(self.obj1, 'y', 0)
        self.assertEqual(0, self.obj1.y)

    def test_update(self):
        """Test update method."""
        self.obj3.update(89)
        self.assertEqual(89, getattr(self.obj3, 'id'))
        self.obj2.update(89, 12)
        self.assertEqual(12, getattr(self.obj2, 'size'))
        self.obj1.update(89, 12, 3)
        self.assertEqual(3, getattr(self.obj1, 'x'))
        self.obj3.update(89, 12, 3, 7)
        self.assertEqual(7, getattr(self.obj3, 'y'))
        self.obj1.update(size=1)
        self.assertEqual(1, getattr(self.obj1, 'size'))
        self.obj2.update(size=6, x=11, y=1, id=50)
        self.assertEqual(1, getattr(self.obj2, 'y'))
        self.assertEqual(6, getattr(self.obj2, 'size'))
        self.assertEqual(11, getattr(self.obj2, 'x'))
        self.assertEqual(50, getattr(self.obj2, 'id'))

        with self.assertRaises((TypeError, ValueError)):
            self.obj4.update(size=None, x=None, y=None)
            self.obj3.update(0)
            self.obj3.update("String")
            self.obj3.update(30, x=-12, y=12)
            self.obj3.update(30, x="Str", y=12)
            self.obj3.update(30, 12, -13)
            self.obj3.update(30, 12, "String")
            self.obj3.update(30, 15, 17, 56, 71)
