#!/usr/bin/python3
"""json string module"""

from json import loads


def from_json_string(my_str):
    """from_json_string
    THIS FUNCTION TAKES JSON OBJECT
    arges:
        my_str: string json obj
    """

    return loads(my_str)
