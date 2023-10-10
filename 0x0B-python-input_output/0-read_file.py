#!/usr/bin/python3
"""Function that reads content from a file."""


def read_file(filename="my_file_0.txt"):
    """
    Read the contents of a text file and print it.

    Args:
        filename (str): The name of the file.

    Raises:
        Exception: When the file cannot be opened.
    """

    with open(filename, 'r', encoding="utf-8") as file:
        read_content = file.read()
        print(read_content)
