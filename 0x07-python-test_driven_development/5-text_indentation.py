#!/usr/bin/python3
"""
This function prints a text string.
"""


def text_indentation(text):
    """
    This function prints a text string.

    Args:
        text (str): The text to be formatted and printed.

    Returns:
        None
    """


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    separators = [".", "?", ":"]
    f_text = text
    for i in separators:
        f_text = f_text.replace(i, i + "\n\n")

    print(f_text[:-3], end="")
