#!/usr/bin/python3
"""This script adds all arguments to a list and saves them to a file."""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    lst = argv[1:]
    filename = "add_item.json"
    try:
        loaded = load_from_json_file(filename)
        lst = loaded + lst
    except FileNotFoundError:
        pass
    save_to_json_file(lst, filename)
