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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square class."""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs["id"]
            if 'size' in kwargs:
                self.size = kwargs["size"]
            if 'x' in kwargs:
                self.x = kwargs["x"]
            if 'y' in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """Magic method.

        Print string representation of square object
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """Represent of square instance in dictionary."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
