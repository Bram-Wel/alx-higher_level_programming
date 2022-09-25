#!/usr/bin/python3
"""Definition of Square class"""


class Square:
    """A square object.

    Attribute:
        size(Int): Size of the square.
    """

    def __init__(self, size=0):
        """Initrializtion of new objects.

        Args:
            size: Square Size, Default value = 0.
        """

        if isinstance(size, int):

            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
