#!/usr/bin/python3
"""Defines a class as Square"""


class Square:
    """ Represents a square"""

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (__int__): Size of the class square
        """

        self.size = size
        

    def area(self):

        """ Returns the current square area """

        return (self.__size) ** 2
      @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
