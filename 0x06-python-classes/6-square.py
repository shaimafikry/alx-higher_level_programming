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
def __init__(self, position=0):
        """initilizations
        Args:
            Self (position): square position
        """
        if not isinstance(position, int):
            raise TypeError("position must be an integer")
        if position < 0:
            raise ValueError("position must be >= 0")
        else:
            self.__position = position


    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.
        Returns:
        - int: The size of the square.
        """
        return self.__size

    def area(self):
        """return sqare area
        Args:
        - no args
        Return:
        square area
        """
        return self.__size ** 2
def position(self):
        """
        Getter method to retrieve the size attribute.
        Returns:
        -position
        """
        return self.__position

    def __init__(self, size=0, position=(0, 0)):

        """

        Args:
        - no args
        Return:
        square area
        """
        
         def my_print(self):
        """print the square to stdout

            Args: no args
        """
        m = 0
        for i in range(self.area()):
            m += 1
            print("#", end="")
            if m == self.size:
                print()
                m = 0
        if (self.size == 0):
            print()
         
