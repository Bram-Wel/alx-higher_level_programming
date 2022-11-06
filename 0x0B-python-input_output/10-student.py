#!/usr/bin/python3
"""This module defines a Student class."""


class Student:
    """The Student Class.

    Attributes:
        first_name (str): Student's first name
        last_name (str): Student's last name
        age (int): The student's age
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Find a dictionary representation of a student instance.

        Retrieves only attributes contained within the list attrs.

        Args:
            attrs (list): List of strings
        Return:
            Dictionary representation of object instance
        """
        dct = self.__dict__
        if attrs is not None:
            return {i: dct[i] for i in dct if i in attrs}
        return self.__dict__
