#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for ```max_integer(list=[])```
    """
    def setUp(self):
        """Setting up the test class
        """
        self.mdoc = __import__('6-max_integer').__doc__

    def tearDown(self):
        """Cleans up test class instance
        """
        pass

    def test_mdocs(self):
        """Check for module documentation
        """
        self.assertTrue(len(self.mdoc) > 1)

    def test_fdocs(self):
        """Check for function documentation
        """
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        """Checks that a list is empty
        """
        new_list = []
        self.assertIsNone(max_integer(new_list))

    def test_args(self):
        """Checks that arguments have been passed to
            ```max_integer(list=[])```
        """
        self.assertIsNone(max_integer())

    def test_single_item(self):
        """Tests for when the list has one item"""
        new_list = [16]
        self.assertEqual(max_integer(new_list), 16)

    def test_none(self):
        """Tests for null(None) argument
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_type(self):
        """Checks for non-integer arguments
        """
        new_list = [16, "Bram", 17, 'v', 89]
        with self.assertRaises(TypeError):
            max_integer(new_list)

    def test_negative(self):
        """Tests for a list of negative values
        """
        new_list = [-6, -5, -12, -199]
        self.assertEqual(max_integer(new_list), -5)

    def test_positive(self):
        """Tests for a list of positive values
        """
        new_list = [1, 100, 102, 165, 216, 93, 21]
        self.assertEqual(max_integer(new_list), 216)


if __name__ == 'main':
    unittest.main(verbosity=2)
