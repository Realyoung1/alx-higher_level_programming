#!/usr/bin/python3
"""Defines Rectangles Classes.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Modules Representation of Squared.
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Squares.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """modules Square size getters.
        """
        return self.width

    @size.setter
    def size(self, value):
        """modules Squares size setters.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """moduled strings represation of squares.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """modules update squared.
        """
        if len(args):
            for q, arg in enumerate(args):
                if q == 0:
                    self.id = arg
                elif q == 1:
                    self.size = arg
                elif q == 2:
                    self.x = arg
                elif q == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """retrun dictonary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
