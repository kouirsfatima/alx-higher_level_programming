#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to be converted to JSON.
        filename (str): The name of the file to write.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other file-related errors.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
