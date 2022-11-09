#!/usr/bin/python3
"""This module describes a test class for the rectangle package."""


import unittest
import io
import sys

from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """A test case class for the Rectangle class."""

    def setUp(self):
        """Create Rectangle instances."""
        self.obj1 = Rectangle(10, 5)
        self.obj2 = Rectangle(10, 5, 3, 6)
        self.obj3 = Rectangle(10, 5, 3, 6, 25)

    # @unittest.skip("")
    def tearDown(self):
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
        self.obj3.update()
        self.assertEqual(18239456, getattr(self.obj3, 'id'))

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
            setattr(self.obj1, 'height', 16.04)

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

        # Test extra argument given
        with self.assertRaises(TypeError):
            self.obj1.area(17)

    def test_update(self):
        """Test update method."""
        self.obj3.update(89)
        self.assertEqual(89, getattr(self.obj3, 'id'))
        self.obj2.update(89, 12)
        self.assertEqual(12, getattr(self.obj2, 'width'))
        self.obj1.update(89, 12, 3)
        self.assertEqual(3, getattr(self.obj1, 'height'))
        self.obj3.update(89, 12, 3, 7)
        self.assertEqual(7, getattr(self.obj3, 'x'))
        self.obj2.update(89, 12, 3, 7, 9)
        self.assertEqual(9, getattr(self.obj2, 'y'))
        self.obj1.update(height=1)
        self.assertEqual(1, getattr(self.obj1, 'height'))
        self.obj2.update(width=6, x=11, y=1, height=2, id=50)
        self.assertEqual(1, getattr(self.obj2, 'y'))
        self.assertEqual(6, getattr(self.obj2, 'width'))
        self.assertEqual(11, getattr(self.obj2, 'x'))
        self.assertEqual(2, getattr(self.obj2, 'height'))
        self.assertEqual(50, getattr(self.obj2, 'id'))


class TestRectangle_stdout(unittest.TestCase):
    """Test the __str__ and display() methods of the Rectangle Class."""

    @classmethod
    def setUpClass(cls):
        """Set up Rectangle instances for the class."""
        cls.obj1 = Rectangle(8, 4)
        cls.obj2 = Rectangle(8, 4, 2)
        cls.obj3 = Rectangle(8, 4, 2, 4)
        cls.obj4 = Rectangle(8, 4, 2, 4, 21)

    @classmethod
    def tearDownClass(cls):
        """Destroy Rectangle instances."""
        del cls.obj1
        del cls.obj2
        del cls.obj3
        del cls.obj4

    @staticmethod
    def capture_stdout(rect, method):
        """Capture and return text written to stdout.

        Args:
            rect (Rectangle): Rectangle printed to stdout
            method (str): Method to run on the rectangle
        Return:
            The text printed to stdout by calling method
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_(self):
        cls = type(self)
        capture = TestRectangle_stdout.capture_stdout(cls.obj1, "print")
        correct = f"[Rectangle] ({cls.obj1.id}) 0/0 - 8/4\n"
        self.assertEqual(correct, capture.getvalue())
        correct = f"[Rectangle] ({cls.obj2.id}) 2/0 - 8/4"
        self.assertEqual(correct, cls.obj2.__str__())
        correct = f"[Rectangle] ({cls.obj3.id}) 2/4 - 8/4"
        self.assertEqual(correct, str(cls.obj3))
        correct = f"[Rectangle] ({21}) 2/4 - 8/4"
        self.assertEqual(correct, str(cls.obj4))

    def test_display(self):
        """Test display."""
        cls = type(self)
        capture = cls.capture_stdout(cls.obj1, "display")
        self.assertEqual("########\n########\n########\n########\n",
                         capture.getvalue())
        capture = cls.capture_stdout(cls.obj2, "display")
        self.assertEqual("  ########\n  ########\n  ########\n  ########\n",
                         capture.getvalue())
        capture = cls.capture_stdout(cls.obj3, "display")
        self.assertEqual("\n\n\n\n  ########\n  ########\n  ########\n"
                         + "  ########\n", capture.getvalue())
