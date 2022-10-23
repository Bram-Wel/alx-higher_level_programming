#!/usr/bin/python3
"""This module defines a Class"""


class BaseGeometry:
    """A Base Class"""

    def __init__(self):
        """Initialisation Function"""
        pass

    def area(self):
        """Geomatrical area of object/surface"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates @value"""
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        elif value < 1:
            raise ValueError(name + ' must be greater than 0')
