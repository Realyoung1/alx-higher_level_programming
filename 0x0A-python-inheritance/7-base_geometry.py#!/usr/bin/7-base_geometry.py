#!/usr/bin/python3
"""Defining the a base geometry class BaseGeo metry."""


class BaseGeometry:
    """Reprsenting the base geo metry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating the a parameter as an integer.

        Args:
            name (str): The name of the parameters...
            value (int): The parameter to validates...
        Raises:
            TypeError: If value is not an integers...
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
