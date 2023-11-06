#!/usr/bin/python3
""" Rectangle module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """init"""
        self._width = width
        self._height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self._width * self._height

    def __str__(self):
        """Rectangle string"""
        return f"[Rectangle] {self._width}/{self._height}"
