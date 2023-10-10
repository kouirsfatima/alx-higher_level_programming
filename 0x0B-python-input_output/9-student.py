#!/usr/bin/python3
"""class student"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
