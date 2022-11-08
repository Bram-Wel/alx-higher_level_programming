#!/usr/bin/python3
"""This module describes the base class of the project.

Python Almost a circle.
"""


class Base:
    """A base class to manage some attributes of its subclasses.

    This base class specifically manages the `id` attribute thereby avoiding
    duplication of code and/or bugs.

    Attributes:
        nb_objects (int): The number of objects/instances
        id (int): Id of an object instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise an object instance.

        Args:
            id (int): Id of the initialising instance
        """
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
