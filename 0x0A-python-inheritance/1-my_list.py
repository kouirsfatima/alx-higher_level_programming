#!/usr/bin/python3
"""This function prints the list, but sorted."""


class MyList(list):
    def print_sorted(self):
        """Print the list, but sorted."""
        print(sorted(self))
