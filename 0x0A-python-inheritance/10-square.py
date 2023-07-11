#!/usr/bin/python3

"""
more class basess ..
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square classess..
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiationing with sizes """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
