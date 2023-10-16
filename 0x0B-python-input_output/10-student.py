#!/usr/bin/python3
"""class student"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()

        if attrs is None:
            return obj

        if not isinstance(attrs, list):
            return obj

        new_dict = {}
        for str_1 in attrs:
            if not isinstance(str_1, str):
                return obj

        for str_1 in attrs:
            if str_1 in obj:
                new_dict[str_1] = obj[str_1]

        return new_dict
