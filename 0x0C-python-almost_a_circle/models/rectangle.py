#!/usr/bin/python3
"""This module describes a subclass of the Base Class."""


from models.base import Base


class Rectangle(Base):
    """This class describes a rectangle object.

    The class inherits from the base class of models.base.

    Args:
        Base (Base): Super class; Base
    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
        x (int): Position on a cartesian axis; (x, y)
        y (int): Position on a cartesian axis; (x, y)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise a rectangle object.

        Args:
            width: Rectangle's width value
            height: Rectangle's height value
            x: X Position
            y: Y Position
            id: Id of object instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Height of the reactangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Position of the rectangle along the X axis.

        Considering the cartesian plane where points are represented on a
        cartesian axis X-Y for 2-D axes.
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Position of the rectangle along the Y axis on cartesian plane."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
