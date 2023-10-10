#!/usr/bin/python3
""" function that returns the JSON representation of an object string."""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object string.
    Args:
        my_obj (object): The object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing the input object.
    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other file-related errors.
    """
    return json.dumps(my_obj)
