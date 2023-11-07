#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """read_file
    args:
        filename: String
    """
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
