#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def write_file(filename="", text=""):
    """open a file and write to it

    Args:
        filename (str, optional): Defaults to "".
    """
    with open(filename, "w", encoding="utf-8") as fe:
        num = fe.write(text)
    return num
