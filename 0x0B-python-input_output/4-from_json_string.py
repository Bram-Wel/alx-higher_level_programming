#!/usr/bin/python3
"""This module describes a json deserialization function."""


import json


def from_json_string(my_str):
    """Decode an object from json string.

    Args:
        my_str: Json string to deserialize/decode
    Return:
        Decoded python object
    """
    return json.loads(my_str)
