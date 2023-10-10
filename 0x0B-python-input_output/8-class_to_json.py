#!/usr/bin/python3
""" function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)for
JSON serialization of an object:."""


def class_to_json(obj):
    """Function that returns the dictionary description of an obj."""
    pld = {}

    if hasattr(obj, "__dict__"):
        pld = obj.__dict__.copy()

    return pld
