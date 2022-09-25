#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """Delete items at a specific position
    in a list

    Args:
        my_list: List to evaluate
        idx: Index of item to remove

    Return: Return changed list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list


if __name__ == "__main__":
    delete_at(my_list=[], idx=0)
