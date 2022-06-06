#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints the integers of a list in reverse

    Args:
        my_list: List to iterate through
    """

    for i in reversed(my_list):
        """if type(i).__name__ == "int":
        """
        print("{:d}".format(i))
