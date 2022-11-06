#!/usr/bin/python3
"""This module describes a json serialization function."""

import json


def save_to_json_file(my_obj, filename):
    """Encode an object in json format.

    The object is written to a text file (Always 'utf-8').

    Args:
        my_obj: Object to serialize/encode
        filename: Name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
