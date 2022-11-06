#!/usr/bin/python3
"""This module describes a serialisation functuion."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure for Json
        serialisation of an object.

    Args:
        obj: Python object
    Return: Return the dictionary description with simple data structure for
    Json serialisation of an object
    """
    return obj.__dict__
