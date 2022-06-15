#!/usr/bin/python3

import sys

length = len(sys.argv)

def print_args(length):
    """Prints No. of arguments & lists them

    """

    if len(sys.argv) == 1:
        print(f"{length - 1} arguments.")
    elif len(sys.argv) == 2:
        print(f"{length - 1} argument:\n{length - 1}: {sys.argv[1]}")
    else:
        print(f"{length - 1} arguments:")
        for i in range(length):
            if sys.argv[i] == sys.argv[0]:
                continue
            print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    print_args(length)
