#!/usr/bin/python3
"""division module
    """


def matrix_divided(matrix, div):
    """divide elements in matrix

    Args:
        matrix (list of lists):
        div (int): division num

    Raises:
        TypeError: if matrix not a list of elemnt not int or float
                    if row are not same length
        ZeroDivisionError: if div was zero

    """

    if not all(isinstance(k, list) for k in matrix):
        raise TypeError(
            "matrix must be a matrix list of lists) of integers/floats")
    # makes matrix as one list to check every elemnt
    flattened = [item for sublist in matrix for item in sublist]
    if not all(isinstance(item, (int, float)) for item in flattened):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]
    i = 0
    n = 0
    for m1 in matrix:
        for k1 in m1:
            new_matrix[i][n] = round(k1 / div, 2)
            n += 1
        i += 1
        n = 0

    return new_matrix
