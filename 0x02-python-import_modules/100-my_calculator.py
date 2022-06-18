#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def calculate():
    """Handles basic Calculator operations
    """

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in "+-*/":
        print(f"Unknown Operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[2] == '+':
        print(f"{sys.argv[1]} + {sys.argv[3]} = ", end="")
        print(f"{add(int(sys.argv[1]), int(sys.argv[3]))}")
    elif sys.argv[2] == '-':
        print(f"{sys.argv[1]} - {sys.argv[3]} = ", end="")
        print(f"{sub(int(sys.argv[1]), int(sys.argv[3]))}")
    elif sys.argv[2] == '*':
        print(f"{sys.argv[1]} * {sys.argv[3]} = ", end="")
        print(f"{mul(int(sys.argv[1]), int(sys.argv[3]))}")
    elif sys.argv[2] == '/':
        print(f"{sys.argv[1]} / {sys.argv[3]} = ", end="")
        print(f"{div(int(sys.argv[1]), int(sys.argv[3]))}")


if __name__ == "__main__":
    calculate()
