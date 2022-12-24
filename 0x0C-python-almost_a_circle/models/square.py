#!/usr/bin/python3
"""This module describes the square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square is a subclass of the Rectangle class.

    The width and height are equal.

    Args:
        Rectangle (Rectangle): The Square super class
    Attributes:
        id (int): Object id
        size (int): Length of the square side
        x (int): X position on a cartesian axis; (x,y)
        y (int): Y position on a cartesian axis; (x,y)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initiaise the square object."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size of the square.

        Inherits the width & height properties from Rectangle class
        """
        return self.width

    @size.setter
    def size(self, value):
        super().width = value
        super().height = value

    def __str__(self):
        """Magic method.

        Print string representation of square object
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
