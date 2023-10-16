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

        result_dict = {}
        for attr in attrs:

            if not isinstance(attr, str):
                return obj

        for attr in attrs:
            if attr in obj:
                result_dict[attr] = obj[attr]

        return result_dict

    def reload_from_json(self, json_data):
        """ Method that replaces all attributes of the Student instance """
        if type (json_data)is  dict:
            obj =  self.__dict__ = json_data
        return obj
