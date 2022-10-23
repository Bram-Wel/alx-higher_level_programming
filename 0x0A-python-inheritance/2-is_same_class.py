#!/usr/bin/python3
"""The module defines an evaluating function """


def is_same_class(obj, a_class):
    """Evaluates if an object is an instance of a class

    Args:
        obj: Object to evaluate
        a_class: Susspect class
    """
    return type(obj) == a_class
