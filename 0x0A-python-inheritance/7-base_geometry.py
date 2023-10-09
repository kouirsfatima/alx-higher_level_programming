#!/usr/bin/python3
"""Base geometry class"""


class BaseGeometry:
    """Base class"""

    def area(self):
        """Method to calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate an integer value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
