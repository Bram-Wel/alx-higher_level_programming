#!/usr/bin/python3
"""This module describes a file reading function."""


def read_file(filename=""):
    """Read a text file, using encoding utf-8 then print contents to stdout.

    Args:
        @filename: Name of file to read
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    pass
