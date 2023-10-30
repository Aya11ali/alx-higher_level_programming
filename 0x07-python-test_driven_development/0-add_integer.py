#!/usr/bin/python3
"""add integerrr module"""


def add_integer(a, b=98):
    """Return: the addition of a + b
    Arges:
        a: int or float
        b: int or float
    """
    if b is None or not isinstance(b, (int, float):
        raise TypeError("b must be an integer")
    if a is None or not isinstance(a, (int, float):
        raise TypeError("a must be an integer")

    minn = -((2 ** 31) - 1) - 1
    maxx = (2 ** 31) - 1

    if b > maxx or a > maxx or b < minn or a < minn:
        raise OverflowError(
            "float overflow : int too large to convert to flaot")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

