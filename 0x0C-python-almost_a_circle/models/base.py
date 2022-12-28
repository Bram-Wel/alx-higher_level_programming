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
        """Return json string representing list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries representing
            object
        Return:
            json string
        """
        if list_dictionaries is None or list_dictionaries == []:
            rt = "[]"
        else:
            rt = json.dumps(list_dictionaries)
        return rt

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json string to file.

        Args:
            list_objs (list): List of objects to serialise
        """
        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            with open(filename, 'w+') as file:
                file.write("[]")
        else:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            with open(filename, 'w+') as file:
                # json.dump(obj_list, file)
                file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Load objects from json string.

        Args:
            json_string (json): A json representation of objects
        Return:
            List of objects
        """
        if not json_string or json_string == []:
            rt = []
        else:
            rt = json.loads(json_string)
        return rt
