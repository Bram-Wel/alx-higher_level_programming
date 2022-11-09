#!/usr/bin/python3
"""This module describes a test class for the rectangle package."""


import unittest

from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """A test case class for the Rectangle class."""

    def setUp(self):
        """Create Rectangle instances."""
        self.obj1 = Rectangle(10, 5)
        self.obj2 = Rectangle(10, 5, 3, 6)
        self.obj3 = Rectangle(10, 5, 3, 6, 25)

    # @unittest.skip("")
    def teardown(self):
        """Destroy Rectangle instances."""
        del self.obj1
        del self.obj2
        del self.obj3

    def test_init(self):
        """Test initialisation of Rectangle objects."""
        self.assertIsNotNone(self.obj1.id)
        self.assertIsNotNone(self.obj2.id)
        self.assertEqual(25, self.obj3.id)  # test super() call
        self.assertEqual(self.obj1.id, self.obj2.id - 1)
        self.assertEqual(10, self.obj1.width)
        self.assertEqual(5, self.obj2.height)
        self.assertEqual(3, self.obj3.x)
        self.assertEqual(6, self.obj3.y)

        # More than 5 arguments
        with self.assertRaises(TypeError):
            self.obj1 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_getsetops(self):
        """Test get and set operations."""
        self.obj1 = Rectangle(8, 4, 0, 2, 17)
        self.assertEqual(17, self.obj1.id)
        self.assertEqual(8, self.obj1.width)
        self.assertEqual(4, self.obj1.height)
        self.assertEqual(0, self.obj1.x)
        self.assertEqual(2, self.obj1.y)
        setattr(self.obj2, 'x', 12)
        self.assertEqual(12, getattr(self.obj2, "x"))
        setattr(self.obj3, 'test', "Test adding attribute")
        self.assertIn('test', dir(self.obj3), msg="test attribute not added")

    @unittest.expectedFailure
    def test_expectedFails():
        """Expected failures."""
        # Check for unset attribute.
        self.assertIn('test_1', dir(self.obj3), msg="test attribute not added")

    def test_private(self):
        """Test that the attributes are private."""
        with self.assertRaises(AttributeError):
            print(self.obj1.__width)
            print(self.obj2.__height)
            print(self.obj3.__x)
            print(self.obj2.__y)

    def test_setters(self):
        """Test that setter conditions are satisfied."""
        # check if values are integers
        with self.assertRaises(TypeError):
            setattr(self.obj1, 'x', "String")
            setattr(self.obj2, 'y', ["lists", 12])
            setattr(self.obj3, 'width', ())
            setattr(self.obj1, 'height', "test")

        # check if width and height are greater than 0
        with self.assertRaises(ValueError):
            setattr(self.obj1, 'width', 0)
            setattr(self.obj2, 'width', -1)
            setattr(self.obj3, 'height', 0)
            setattr(self.obj2, 'height', -12)

        # check if x and y are 0 or greater
        with self.assertRaises(ValueError):
            setattr(self.obj2, 'x', -1)
            setattr(self.obj3, 'y', -100)
        setattr(self.obj1, 'x', 0)
        self.assertEqual(0, self.obj1.x)
        setattr(self.obj2, 'y', 0)
        self.assertEqual(0, self.obj2.y)

    def test_area(self):
        """Test area method."""
        self.assertEqual(50, self.obj1.area())
        self.assertEqual(50, self.obj2.area())
        self.assertEqual(50, self.obj3.area())
