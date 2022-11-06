#!/usr/bin/python3
"""This module describes a json serialization function."""


import json

def to_json_string(my_obj):
    """Encode an object in json format.

    Args:
        my_obj: Object to serialize/encode
    Return:
        Encoded json string of the object
    """
    return json.dumps(my_obj)
