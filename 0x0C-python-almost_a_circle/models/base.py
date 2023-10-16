#!/usr/bin/python3
#!/usr/bin/python3
"""
import json
import csv
"""
import json
import csv

"""module Base"""


class Base:
    """This class represent a Base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base Object.
        Args:
            id (int): The ident of The Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries.

        If list_dictionaries is None or  an empty list return '[]'.
        Overwrite json string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        str_dict = json.dumps(list_dictionaries)
        return str_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances to be saved.

        If list_objs is None, save an empty list.
        Overwrite the file if it already exists.
        """
        _list = []
        if list_objs is not None:
            for obj in list_objs:
                _list.append(obj.to_dictionary())

        filename = f"{cls.__name__}.json"
        json_str = cls.to_json_string(_list)

        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on
            the provided dictionary.
        Args:
            **dictionary: a double pointer to a dictionary

        Return:
            Instance of the class with attributes set.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

