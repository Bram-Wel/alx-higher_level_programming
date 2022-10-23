#!/usr/bin/python3
"""Defines a subclass"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that is subclass to BaseGeometry

    Attributes:
        @width: (int) Width of rectangle object
        @height: (int) Height of rectangle object
    """

    def __init__(self, width, height):
        """Initialises the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the Area of a rectangle

        Return:
            Area of the rectangle object
        """

        return self.__height * self.__width

    def __str__(self):
        """String magic method.

        Return:
            A string representation of the object
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
