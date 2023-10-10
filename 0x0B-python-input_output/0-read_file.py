#!/usr/bin/python3
def read_file(filename="my_file_0.txt"):
    """Read the contents of a text file and print it."""
    with open(filename, 'r', encoding="utf-8") as file:
        read_file = file.read()
        print(read_file)
        return read_file
