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
        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

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
        symbol_line = str(Rectangle.print_symbol) * self.width
        return "\n".join([symbol_line for _ in range(self.height)])

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
