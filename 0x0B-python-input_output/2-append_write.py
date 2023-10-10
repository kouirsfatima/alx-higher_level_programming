#!/usr/bin/python3
"""function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """
 function that appends a string at the end of a text file
 and returns the number of characters added
    Args:
        filename (str): The name of the file.
        text (str): The text to be append.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other file-related errors.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file_append = file.write(text)
        return file_append
