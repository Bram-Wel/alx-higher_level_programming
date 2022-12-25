#!/usr/bin/python3
"""This module describes a subclass of the Base Class."""


from models.base import Base


class Rectangle(Base):
    """This class describes a rectangle object.

    The class inherits from the base class of models.base.

    Args:
        Base (Base): Super class; Base
    Attributes:
        id (int): Id of rectangle object
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
        """Width of the rectangle.

        Raise:
            TypeError: If width is not an integer
            ValueError: If width is less than or equal to 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height of the rectangle.

        Raise:
            TypeError: If height is not an integer
            ValueError: If height is less than or equal to 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Position of the rectangle along the X axis.

        Considering the cartesian plane where points are represented on a
        cartesian axis X-Y for 2-D axes.
        Raise:
            TypeError: If x is not an integer
            ValueError: If x is less than 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Position of the rectangle along the Y axis on cartesian plane.

        Raise:
            TypeError: If y is not an integer
            ValueError: If y is less than 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Find the area of a rectangle object.

        Return:
            The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """Print the rectangle instance to stdout.

        Prints using the # character.
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """Update the Rectangle class.

        Takes positional & keyword args.
        Args:
            args[0]: Id
            args[1]: width
            args[2]: height
            args[3]: x
            args[4]: y
        """
        if args:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs["id"]
            if 'width' in kwargs:
                self.__width = kwargs["width"]
            if 'height' in kwargs:
                self.__height = kwargs["height"]
            if 'x' in kwargs:
                self.__x = kwargs["x"]
            if 'y' in kwargs:
                self.__y = kwargs["y"]

    def __str__(self):
        """Print a string describing the object."""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                + f" - {self.__width}/{self.__height}")

    def to_dictionary(self):
        """Represent of rectangle instance in dictionary."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
