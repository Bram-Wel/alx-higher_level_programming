#!/usr/bin/python3
"""This module defines a printing function"""


def say_my_name(first_name, last_name=""):
    """Prints the 1st & 2nd name in string

    Args:
        first_name: The 1st Name
        last_name: 2nd Name (Defaults to an empty string).
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
