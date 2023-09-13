#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    sorted_keys = a_dictionary.keys()
    for key in sorted_keys:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
