#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init
        Args:
            width: int
            height: int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method
           checking width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method
           checking height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returns a rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rec = ((self.width * f"{self.print_symbol}" + "\n") * self.height).rstrip()
        return rec

    def __repr__(self):
        """return rectangle arguments"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print delete messageeee"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal
        Args:
            rect_1: rectangle instance
            rect_2: rectangle instance
        Return:
            bigger rectangle or rect_1 if they are eqqual
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """square
        Args:
            size: width == height == size
        Retrun:
            new object for rectangle
        """
        return Rectangle(size, size)
