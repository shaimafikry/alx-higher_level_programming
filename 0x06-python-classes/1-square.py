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
    def __init__(Self, __size = 0):
        """initilizations

        Args:
            Self (size): square size
        """
        

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
