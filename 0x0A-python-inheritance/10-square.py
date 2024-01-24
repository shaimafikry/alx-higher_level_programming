#!/usr/bin/python3
"""rectangle class iherts from geometry

    """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """class square
    Args:
        rectangle (base class): base class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
