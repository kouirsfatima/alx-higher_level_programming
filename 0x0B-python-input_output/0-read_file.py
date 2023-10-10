#!/usr/bin/python3
"""Function that reads content from a file."""


def read_file(filename="my_file_0.txt"):
    """
    Read the contents of a text file and print it.

    Args:
        filename : The name of the file.

    Raises:
        Exception: When the file cannot be opened.
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')