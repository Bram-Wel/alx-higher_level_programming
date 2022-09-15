#!/usr/bin/python3
"""Function definitions."""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: 1st Integer/Float
        b: 2nd Integer/Float (Defaults to 98).

    Return:
        Integer sum of a & b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
