#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in i:
            if x == i[len(i) - 1]:
                print("{:d}".format(x))
            else:
                print("{:d}".format(x), end=" ")
