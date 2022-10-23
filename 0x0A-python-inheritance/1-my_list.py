#!/usr/bin/python3
"""Defines an inherited class"""


class MyList(list):
    """A list class that inherits from the list module"""

    def __init__(self):
        """Initialise the class"""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
