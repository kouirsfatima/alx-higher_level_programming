#!/usr/bin/python3
"""Function that reads content from a file."""


def read_file(filename=""):
    """
    Read the contents of a text file and print it.

    Args:
        filename (str): The name of the file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: For other file-related errors.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end=" ")
