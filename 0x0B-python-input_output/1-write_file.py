#!/usr/bin/python3
"""module for  Python - Input/Output
    """


def write_file(filename="", text=""):
    """open a file and read it and print it to stdout

    Args:
        filename (str, optional): Defaults to "".
    """
    with open(filename, "w", encoding="utf-8") as fe:
        num = fe.write(text)
    return num

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
