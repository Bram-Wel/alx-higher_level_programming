#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer

    Args:
        @value: Value to print

    Return: True when value is an integer, False otherwise
    """

    try:
        print("{:d}".format(value))
    except BaseException:
        return (False)
    else:
        return (True)

if __name__ == "__main__":
    safe_print_integer(value)
