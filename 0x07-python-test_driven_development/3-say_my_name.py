#!/usr/bin/python3
"""
    This function prints a formatted string.

"""


def say_my_name(first_name, last_name=""):
    """

    This function prints a formatted string.


    Args:
        first_name : The first name.
        last_name : The last name.

    Returns:
        str: The formatted string "My name is <first name> <last name>".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
