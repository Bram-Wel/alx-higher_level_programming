#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves elements from a list in C format

    Args:
        my_list: LIst to Iterate
        idx: Index from which to retrieve element

    Return: None if negative index or out of range index
    """

    if idx < 0 or idx >= len(my_list):
        return

    return (my_list[idx])

if __name__ == "__main__":
    element_at(my_list, idx)
