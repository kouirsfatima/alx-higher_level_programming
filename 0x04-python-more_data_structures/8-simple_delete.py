#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        a_dictionary.popitem()
    sorted_keys = sorted(a_dictionary.keys())
    for i in sorted_keys:
        return (a_dictionary)
