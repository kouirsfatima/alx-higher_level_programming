#!/usr/bin/python3
def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size of the square.

    Raises:
        ValueError: If size is not a positive integer.
        TypeError: If size is not an integer.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be a positive integer")

    for i in range(size):
        print("#" * size)
