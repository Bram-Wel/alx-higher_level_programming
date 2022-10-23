#!/usr/bin/python3
"""Defines a subclass"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A rectangle class that is subclass to BaseGeometry

    Attributes:
        @size: (int) Width/side length of square object
    """

    def __init__(self, size):
        """Initialises the class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate area of a square"""
        return super().area()

    def __str__(self):
        """String magic method

        Return:
            String representation of Square[Unofficial]
        """

        return f"[Square] {self.__size}/{self.__size}"
