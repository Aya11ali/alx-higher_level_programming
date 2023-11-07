#!/usr/bin/python3
"""Append Text Module"""


def append_write(filename="", text=""):
    """append_write
    arges:
        filename: String
        text: String To Append
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
