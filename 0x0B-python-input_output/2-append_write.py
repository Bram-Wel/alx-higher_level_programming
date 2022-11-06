#!/usr/bin/python3
"""This module describes a function that writes to a stream object."""


def append_write(filename="", text=""):
    """Append a string of text to a file in 'utf-8'.

    The function appends to the end of the file if it
    already exists or creates a new one otherwise.

    Args:
        @filename: Name of file to write
        @text: The string of text written to file
    Return:
        Number of characters that are written
    """
    with open(filename, 'a', encoding='utf-8') as file:
        no = file.write(text)
    return no
