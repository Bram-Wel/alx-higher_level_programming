#!/usr/bin/python3

from hidden_4 import *
list = dir()


def print_cpy(list):
    """Print all names defined in a compiled module excluding
    those starting with __
    """

    for i in list:
        if i[0] != '_' and i[1] != '_':
            print(i)


if __name__ == "__main__":
    print_cpy(list)
