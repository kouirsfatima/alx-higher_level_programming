#!/usr/bin/python3
"""Create a Square class with a private attribute size"""


class Square:
    """Initialize the Square class with a private attribute size"""

    def __init__(self, size=0):
        """Initialize a square with the given size.
        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
