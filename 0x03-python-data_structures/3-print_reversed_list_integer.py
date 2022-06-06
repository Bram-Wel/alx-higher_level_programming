#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints the integers of a list

    Args:
        my_list: List to iterate through
    """

    for i in my_list:
        """if type(i).__name__ == "int":
        """
        print("{:d}".format(i))
