#!/usr/bin/python3
"""import Rectange from models.rectangle"""
from models.rectangle import Rectangle

"""module Square"""


class Square(Rectangle):
    """This class represent Square module
        that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize new Square Object
        Args:
            size (int) : The width of The Square
            x (int) : The x of The Square
            y (int) : The y of The Square
            id (int) : The id of The Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return interger size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """set value to The size of Square"""
        self.width = value
        self.height = value

    def __str__(self):
        
        """return string"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
        *args (ints): New attribute values.
            - 1st argument represents id attribute
            - 2nd argument represents width attribute
            - 3rd argument represent height attribute
            - 4th argument represents x attribute
            - 5th argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
