#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Define a Rectangle class."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height."""
        self.width = width
        self.height = height
        type self.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        return rect_1 if area_1 >= area_2 else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with height == width."""
        return cls(width=size, height=size)

    def area(self):
        """Return the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.height == 0 or self.width == 0:
            return ""
        symbol_line = (self.print_symbol) * self.width
        return "\n".join([symbol_line for _ in range(self.height)])

    def __repr__(self):
        """ return a string representation of the rectangle """

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        type self.number_of_instances -= 1
        print("Bye rectangle...")
