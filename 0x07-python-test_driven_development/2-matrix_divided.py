#!/usr/bin/python3
"""Defines a division function for a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: A matrix
        div: The divisor

    Return:
        Resulting matrix
    """

    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(lst, list) for lst in matrix) or
            not all(isinstance(i, (int, float)) for b in matrix for i in b)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    elif not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda m: round(m / div, 2), row)) for row in matrix]
