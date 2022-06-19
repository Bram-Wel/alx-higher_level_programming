#!/usr/bin.python3


def max_integer(my_list=[]):
    """Find the biggest Integer

    Args:
        my_list: List of integers

    Return:
        The largest integer
    """

    if not my_list:
        return None

    big = my_list[0]
    for i in my_list:
        if i > big:
            big = i

    return big


if __name__ == "__main__":
    max_integer(my_list=[])
