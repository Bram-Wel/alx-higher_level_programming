#!/usr/bin/python3
"""Definition of Square class"""


class Square:
    """A square object.

    Attribute:
        size(Int): Size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initrializtion of new objects.

        Args:
            size: Square Size, Default value = 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of square."""
        return self.__size

    @property
    def position(self):
        """Retrieve position of square on x-y axis."""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Sets the values of position."""

        if ((not isinstance(value, tuple)) or len(value) != 2
                or not all(isinstance(i, int) for i in value)
                or not all(i >= 0 for i in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """An instance method

        Return:
            Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints out a square on stdout with
        # on an (a, b) axis.
        """
        for b in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for a in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.size == 0:
            print()
