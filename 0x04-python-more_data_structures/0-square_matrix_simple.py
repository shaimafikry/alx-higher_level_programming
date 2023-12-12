#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        new_list = list(map(lambda i: list(map(lambda x: x ** 2, i)), matrix))
    return new_list
