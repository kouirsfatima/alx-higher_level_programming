#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """Return interger size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value to The size of Square"""
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """return string"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign value to attribute using *args"""
        OrdArgs = ['id', 'size', 'x', 'y']

        if args:
            for idx, value in enumerate(args):
                if value is None:
                    self.__init__(self.size, self.x, self.y)
                if value is not None and idx <= 3:
                    setattr(self, OrdArgs[idx], value)
        else:
            for key, value in kwargs.items():
                if value is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
