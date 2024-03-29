#!/usr/bin/python3
"""Defines a class as Square"""


class Square:
    """ Represents a square"""

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (__int__): Size of the class square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """ Returns the current square area """

        return (self.__size) ** 2
