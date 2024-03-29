#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """An empty Rectangle  class

    Attribute:
        width(int): Width of the rectangle
        height(int): Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialises the rectangle variable

        Args:
            width: Rectangle's width
            height: Rectangle's height
        """
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

    def __del__(self):
        """Cleans up when destroying an instance"""
        print("Bye rectangle...")

    def __str__(self):
        """String representation of the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return "".join(rect)

    def __repr__(self):
        """Official representation of rectangle"""
        width = self.__width
        height = self.__height
        return "Rectangle(" + str(width) + ", " + str(height) + ")"
