#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def append_write(filename="", text=""):
    """open a file and read it and print it to stdout

    Args:
        filename (str, optional): Defaults to "".
    """
    with open(filename, "a", encoding="utf-8") as fe:
        num = fe.write(text)
    return num
