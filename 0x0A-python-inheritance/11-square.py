#!/usr/bin/python3
""" MyInt Module"""


class MyInt(int):
    """ MyInt Class"""

    def __eq__(self, other):
        return int.__ne__(self, other)


    def __ne__(self, other):
        return int.__eq__(self, other)
