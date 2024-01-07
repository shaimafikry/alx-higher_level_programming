#!/usr/bin/python3
"""
This module defines an empty class called Square.
"""


class Square:
    """
    This class represents a geometric square.

    Attributes:
    size: size of square
    """

    def __init__(self, size=0):
        """initilizations

        Args:
            Self (size): square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
