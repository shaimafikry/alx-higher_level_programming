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
        if not isinstance(width, (int)):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, (int)):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
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

    def area(self):
        """return rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """returns rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """represent the object in string when called

        Returns:
            area with #
        """
        prn = ""
        if self.__height == 0 or self.__width == 0:
            return prn
        for i in range(self.__height):
            prn += "#" * self.__width + "\n"
        return prn[:-1]

    def __repr__(self):
        """represent the object in string when called

        Returns:
            area with #
        """
        return f"Rectangle{self.__width, self.__height}"
