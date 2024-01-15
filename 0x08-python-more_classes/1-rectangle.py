#!/usr/bin/python3
"""this module is for rectangle class 
    """


class Rectangle:
    """rectangle class to calculate size
    """

    def __init__(self, width=0, height=0):
        """initiation 
        Args:
            width: int >0
            height: int > 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
