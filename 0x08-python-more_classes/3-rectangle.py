#!/usr/bin/python3
"""Rectangle module.

There is a class called Rectangle in this module that defines a rectangle.

"""


class Rectangle():
    """Rectangle code goes here"""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the Rectangle object.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Sets the print behavior of the Rectangle Object."""
        retangle = ""

        if self.__width > 0 and self.__height > 0:
            for x in range(self.__height):
                retangle += '#' * self.__width + '\n'

        return retangle[:-1]

    @property
    def width(self):
        """Get or set the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the height of a the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        
    def area(self):
        """Returns the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle's perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return self.__height * 2 + self.__width * 2
