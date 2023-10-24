#!/usr/bin/python3
"""square class"""


class Square:
    """square"""

    def __init__(self, size=0):
        """init
        Args:
            size: size of square
        """
        self.size = size

        @property
        def size(self):
            """size getter"""
            return self.__size

        @size.setter
        def size(self, value):
            """size setter"""
            if size < 0:
                raise ValueError("size must be >= 0")
            elif not isinstance(size, int):
                raise TypeError("size must be an integer")

        self.__size = value

    def area(self):
        """area of a square"""
        return self.__size * self.__sizei

    def my_print(self):
        """print a square of #"""
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
