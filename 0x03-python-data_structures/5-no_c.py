#!/usr/bin/python3

def no_c(my_string):
    """Removes c & C characters from a string

    Args:
        my_string: String to copy

    Return:
        The new String
    """

    str = ''

    for i in my_string:
        if i not in 'cC':
            str += i

    return str
