#!/usr/bin/python3
"""  function that returns an object (Python data structure)
represented by a JSON string."""


import json


def from_json_string(my_str):
    """
    Function that returns the JSON representation of an object string.
    Args:
        my_str (object): The object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing the input object.
    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other file-related errors.
    """
    return json.loads(my_str)
