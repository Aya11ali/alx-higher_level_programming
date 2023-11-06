#!/usr/bin/python3
""" Rectangle module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangles class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """init def"""
        self._width = width
        self._height = height
        self.integer_validator("width", self._width)
        self.integer_validator("height", self._height)
