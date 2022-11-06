#!/usr/bin/python3
"""This module describes a json deserialization function."""


import json


def load_from_json_file(filename):
    """Decode an object from json file.

    Args:
        filename: File containing Json String
    Return:
        Decoded python object
    """
    with open(filename, encoding='utf-8') as file:
        obj = json.load(file)
    return obj
