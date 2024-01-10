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
        self.__size = size
        self.__position = position
    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.
        Returns:
        - int: The size of the square.
        """
        return self.__size
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
    @property
    def position(self):
        """
        Getter method to retrieve the size attribute.
        Returns:
        -position
        """
        return self.__position
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
           for i in range (self.__position[1]):
              print()
        for i in range(self.__size):
            if not self.__position[1] >= 0:
                print("_" * self.__position[0] + "#" * self.__size)
            else:
                print(" " * self.__position[0] + "#" * self.__size)

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
