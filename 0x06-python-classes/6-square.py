#!/usr/bin/python3

"""
This module defines a class called Square.
"""


class Square:
    """
    This class represents a geometric square.

    Attributes:
    size: size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initilizations
        Args:
            Self (position): square position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) for i in position) or not all(
            i >= 0 for i in position
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
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

    @property
    def position(self):
        """
        Getter method to retrieve the size attribute.
        Returns:
        -position
        """
        return self.__position

    @size.setter
    def size(self, value):
        """setting the size attribute
        Args:
            Self (size): square size
            vaue : the new size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setting the size attribute
        Args:
            Self (position):
            value : the new position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) for i in value) or not all(
            i >= 0 for i in value
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return sqare area
        Args:
        - no args
        Return:
        square area
        """
        return self.__size ** 2

    def my_print(self):
        """print the square to stdout
            Args: no args
        """
        if self.size == 0:
            print()
            return
        if self.__position[1] > 0:
           for i in range (self.__position[1]:
              print()
        for i in range(self.__size):
            if not self.__position[1] >= 0:
                print("_" * self.__position[0] + "#" * self.__size)
            else:
                print(" " * self.__position[0] + "#" * self.__size)
