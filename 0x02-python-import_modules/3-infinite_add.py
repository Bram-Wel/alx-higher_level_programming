#!/usr/bin/python3

import sys
length = len(sys.argv)


def add_args(length):
    """Adds all arguments to a program and prints the sum
    """

    sum = 0
    if length > 1:
        for i in range(length):
            if i == 0:
                continue
            else:
                sum += int(sys.argv[i])
        print(f"{sum}")
    else:
        print(f"{sum}")


if __name__ == "__main__":
    add_args(length)
