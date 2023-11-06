#!/usr/bin/python3
""" Rectangle module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Rectangles class that inherits from BaseGeometry"""

    def __init__(self, size):
        """init def"""
        self.___size = size
        self.integer_validator("size", self.___size)
        Rectangle.__init__(self, self.___size, self.___size)

    def area(self):
        """Calculates aaand returns the area of the Square"""
        return self.___size ** 2
