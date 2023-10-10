#!/usr/bin/python3
"""Function writes a string to a text file."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns
    the number of characters written.

    Args:
        filename (str): The name of the file.
        text (str): The text to be written.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other file-related errors.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
