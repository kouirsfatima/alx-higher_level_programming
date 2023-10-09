#!/usr/bin/python3
"""returns True if the object is exactly an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False."""


def is_kind_of_class(obj, a_class):
    """returns True if the object is exactly an instance"""
    if isinstance(obj, a_class):
        return True
    elif type(obj) is not a_class:
        return False
