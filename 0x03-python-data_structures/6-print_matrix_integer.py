#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    """Prints a matrix of integers

    Args:
        matrix: A matrix of integers
    """

    if matrix is not None:
        for i in matrix:
            for j in range(len(i) - 1):
                print("{:d}".format(i[j]), end=", ")
            print("{:d}".format(i[len(i) - 1]))
    else:
        print()
