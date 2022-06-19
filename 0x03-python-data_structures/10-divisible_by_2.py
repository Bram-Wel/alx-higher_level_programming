#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds multiples of 2

    Args:
        List of integers

    Return:
        List of true/false for multiples of 2
    """

    return [True if i % 2 == 0 else False for i in my_list]

if __name__ == "__main__":
    divisible_by_2(my_list=[])
