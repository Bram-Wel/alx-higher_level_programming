#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace a list element at index

    Args:
        my_list: List to Alter
        idx: Index of element
        element: Element to append at list index

    Return:
        None if index is negative or out of bounds, or the
        appended list.
    """

    if idx < 0 or idx >= len(my_list):
        return

    my_list[idx] = element
    return (my_list)

if __name__ == "__main__":
    replace_in_list(my_list, idx, element)
