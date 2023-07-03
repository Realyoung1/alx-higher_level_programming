#!/usr/bin/python3
# 4-rectangle.py
"""Defining a rect-angle more classes."""


class Rectangle:
    """Represents a rect-angle more classes"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rect-angle more classes
        Args:
            width (int): this is The width of the new rect-angle more classes.
            height (int): this is The height of the new rectangle more classes.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rect-angle more classes"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rect-angle more classes."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for k in range(self.__height):
            [rect.append('#') for d in range(self.__width)]
            if k != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
