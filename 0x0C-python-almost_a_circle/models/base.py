#!/usr/bin/python3
"""This module describes the base class of the project.

Python Almost a circle.
"""

import json


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

    def __del__(self):
        """Run when the base class is destroyed.

        Reduces the number of initialised instances nb_objects
        """
        try:
            if(self.id >= 0 or self.id <= Base.__nb_objects):
                Base.__nb_objects -= 1
        except AttributeError:
            pass

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json string representing list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            rt = "[]"
        else:
            rt = json.dumps(list_dictionaries)
        return rt
