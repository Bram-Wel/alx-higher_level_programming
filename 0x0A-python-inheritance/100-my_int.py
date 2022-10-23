#!/usr/bin/python3
"""A subclass of int"""


class MyInt(int):
    """Ä user defined class that extends into int"""

    def __new__(cls, *args, **kwargs):
        """Initialise"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Define == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Define != operator"""
        return int(self) == other
