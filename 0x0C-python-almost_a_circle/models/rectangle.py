#!/usr/bin/python3
"""rectangle inherts from base
    """


from .base import Base
import json

class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for the rectangle classs
            inherts "id" from base clasee
        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): Defaults to 0.
            y (int): Defaults to 0.
            id (int): Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    def area(self):
        """returns the area value of rectangle"""
        return self.width * self.height

    def display(self):
        """represent rectangle in #"""
        if (self.y > 0):
            for i in range(self.y):
                print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assign values to attr"""
        if not args:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            attrs = ("id", "width", "height", "x", "y")
            for a, i in zip(attrs, args):
                setattr(self, a, i)
    def to_dictionary(self):
        """returns dict of attribute"""
        return json.dumps(Rectangle())
