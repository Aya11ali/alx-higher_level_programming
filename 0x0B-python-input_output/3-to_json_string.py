#!/usr/bin/python3
"""Json String Module"""

from json import dumps


def to_json_string(my_obj):
    """to_json_string
    This function taks dictionary and convert it to json object
    arges:
        my_obj: Python Dictionary
    """

    return dumps(my_obj)
