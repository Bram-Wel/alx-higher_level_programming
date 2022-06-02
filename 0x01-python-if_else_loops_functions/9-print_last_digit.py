#!/usr/bin/python3


def print_last_digit(number):
    """Print & Return the last digit of a number"""
    def abs_no(n):
        """Return the absolute value of a number"""
        if n < 0:
            return -n
        return n

    last_digit = abs_no(number) % 10
    """
    if number < 0:
        last_digit = -last_digit
    """
    print(f"{last_digit}", end="")
    return last_digit
