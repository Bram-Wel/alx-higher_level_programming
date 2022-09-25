#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element at index without modifying the
        the original list

    Args:
        my_list: List to copy
        idx: Index of element
        element: Element to append on the copy

    Return:
        Copy of the list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    a = my_list[:]
    a[idx] = element
    return a
