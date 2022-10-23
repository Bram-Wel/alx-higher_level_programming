#!/usr/bin/python3
"""Defines a function that adds evaluates objects"""


def add_attribute(obj, att, value):
    """Adds attribute to value"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
