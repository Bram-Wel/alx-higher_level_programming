#!/usr/bin/python3
"""Square printing fxn definitions"""


def print_square(size):
    """Prints a fxn of given size with #

    Args:
        size: size length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
