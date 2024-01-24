#!/usr/bin/python3
Rectangle = __import__('9-rectangle.py').Rectangle
"""
This module defines a Square class that inherits from the Rectangle class.
The Square class represents a square shape with a given size.
It overrides the area method from the Rectangle class to calculate the area of the square.
    """


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
