#!/usr/bin/python3
"""square class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init
        Args:
            size: size of this square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        def area(self):
            """area of this square"""
            return self.__size * self.__size
