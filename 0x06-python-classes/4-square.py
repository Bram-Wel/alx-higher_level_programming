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
        self.size = size

    @property
    def size(self):
        """Retrieve the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size."""

        if isinstance(value, int):

            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """An instance method

        Return:
            Area of the square
        """
        return self.__size ** 2
