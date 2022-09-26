#!/usr/bin/python3
"""This module describes a sorting function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers

    Args:
        list_of_integers: List of unsorted integers

    Return:
        Peak integer in the list
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    lst = list_of_integers
    high = len(lst)
    mid = high // 2
    if high == 1:
        rtn = lst[0]
    elif high == 2:
        rtn = max(lst)
    elif lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
        rtn = lst[mid]
    elif mid > 0 and lst[mid] < lst[mid + 1]:
        rtn = find_peak(lst[mid:])
    elif mid > 0 and lst[mid] < lst[mid - 1]:
        rtn = find_peak(lst[:mid])
    return rtn
