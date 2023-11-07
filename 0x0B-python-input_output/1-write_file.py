#!/usr/bin/python3
"""Write File Module"""


def write_file(filename="", text=""):
    """write_file
    args:
        filename: String
        text: String
    """
    with open(filename, encoding="utf-8", mode="w") as file:
        return file.write(text)
