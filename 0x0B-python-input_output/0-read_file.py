#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def read_file(filename=""):
    """open a file and read it and print it to stdout

    Args:
        filename (str, optional): Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as fe:
        read = fe.read()
    print(read, end="")
