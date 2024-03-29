#!/usr/bin/python3
"""The module defines an evaluating function """


def is_kind_of_class(obj, a_class):
    """Evaluates if an object is an instance of a class

    Args:
        obj: Object to evaluate
        a_class: Susspect class
    """
    return isinstance(obj, a_class)
