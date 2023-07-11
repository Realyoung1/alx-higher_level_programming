#!/usr/bin/python3
"""
this func contain the MyList class
"""


class MyList(list):
    """a subcla of list"""
    def __init__(self):
        """initialize the objt"""
        super().__init__()

    def print_sorted(self):
        """printed the sorted list"""
        print(sorted(self))
