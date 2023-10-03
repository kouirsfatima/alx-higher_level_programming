#!/usr/bin/python3
"""
This function adds two numbers.


"""


def add_integer(a, b=98):

    """This function adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b, converted to an integer.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer or float")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
