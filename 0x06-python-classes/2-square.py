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
        try:
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
