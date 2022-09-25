#!/usr/bin/python3
"""A function definition"""


def magic_string():
    """Returns a magic string
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
