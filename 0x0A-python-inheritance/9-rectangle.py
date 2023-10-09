#!/usr/bin/python3
""" module subclass rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Constructor method for Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method to calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method to represent the Rectangle object as a string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
