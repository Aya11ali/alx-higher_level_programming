#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """class_to_json
    load jssson object from .json file
    arges:
        obj: class instans
    """
    return obj.__dict__
