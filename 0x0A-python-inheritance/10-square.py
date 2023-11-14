#!/usr/bin/python3
""" Module subclass square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Constructor method for Square """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ Method to calculate the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ Method to represent the Square object as a string """
        return f"[Rectangle {self.__size}/{self.__size}"
