#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def append_write(filename="", text=""):
    """open a file and write to it

    Args:
        filename (str, optional): Defaults to "".
    """
    with open(filename, "a", encoding="utf-8") as fe:
        num = fe.write(text)
    return num
