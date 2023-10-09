#!/usr/bin/python3
"""returns True if the object is exactly an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False."""


def inherits_from(obj, a_class):
    """returns True if the object is exactly an instance"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
