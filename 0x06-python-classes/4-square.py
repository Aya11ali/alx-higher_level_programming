#!/usr/bin/python3
"""square class"""


class square:
    """Square"""

    def __init__(self, size=0):
        """init
        Args:
            size: size of this square
        """

        self.size = size

        @property
        def size(self):
            """size bla bla"""
            return self.__size


        @size.setter
        def size(self, value)
        """size bla bla"""
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")

        self.__size = value

        def area(self):
            """bla bla"""
            return self.__size * self.__size
