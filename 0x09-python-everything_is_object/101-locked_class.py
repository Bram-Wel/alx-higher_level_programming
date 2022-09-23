#!/usr/bin/python3
"""Defines an attributeless class"""


class LockedClass:
    """Class that prevents the user from creating dynamic
        instance attributes other than firstname
    """
    __slots__ = ['first_name']
