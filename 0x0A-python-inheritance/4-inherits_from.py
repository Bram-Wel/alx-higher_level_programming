#!/usr/bin/python3
"""The module defines an evaluating function """


def inherits_from(obj, a_class):
    """Evaluates if an object is an instance of a class

    Args:
        obj: Object to evaluate
        a_class: Susspect class
    Return:
        True/False depending on the evaluated result
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
