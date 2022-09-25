#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """An empty Rectangle  class

    Attribute:
        width(int): Width of the rectangle
        height(int): Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialises the rectangle variable"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieves height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value for width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets a height value for the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of a rectangle object

        Return:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Obtains the perimeter of given rectangle

        Return:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            per = 0
        else:
            per = (2 * self.__width) + (2 * self.__height)
        return per
