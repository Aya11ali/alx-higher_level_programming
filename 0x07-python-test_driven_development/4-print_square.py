#!/usr/bin/python3
"""print square module"""


def print_square(size):
    """prints a square with the character #
    Arges:
        size: int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size == 0:
        return ""
    if size < 0:
        raise ValueError("size must be >= 0")
    rectangle = (("#" * size + "\n") * size).rstrip()
    print(rectangle)
