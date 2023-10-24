#!/usr/bin/python3
"""square class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init
        Args:
            size: size of square
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")

        self.__size = size

    def area(self):
        """area of a square"""
        return self.__size * self.__size
