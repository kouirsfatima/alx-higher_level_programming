#!/usr/bin/python3
"""Create a Square class with a private attribute size"""

class Square:
    """Initialize the Square class with a private attribute size"""

    def __init__(self, size):
        """Initialize a square with the given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
