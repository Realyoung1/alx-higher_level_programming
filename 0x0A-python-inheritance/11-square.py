#!/usr/bin/python3

"""
more class baseess ...
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square classess ...
"""


class Square(Rectangle):
    """ Squared Classes """
    def __init__(self, size):
        """ size init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
