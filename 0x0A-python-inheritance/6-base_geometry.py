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
