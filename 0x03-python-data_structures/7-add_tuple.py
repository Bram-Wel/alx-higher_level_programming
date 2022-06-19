#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tupples

    Args:
        tuple_a: 1st tuple
        tuple_b: 2nd tuple

    Return: tuple of integers
    """

    new = 0,
    if len(tuple_a) < 2:
        if len(tuple_a) > 0:
            tuple_a = tuple_a + new
        else:
            tuple_a = 0, 0
    if len(tuple_b) < 2:
        if len(tuple_b) > 0:
            tuple_b = tuple_b + new
        else:
            tuple_b = 0, 0

    t = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return t


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
