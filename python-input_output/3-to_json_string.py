#!/usr/bin/python3
"""
This script defines a function to convert Python objects to JSON strings.

The function `to_json_string` takes a Python object as input and returns its
JSON representation.
"""


import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON representation of the Python object.
    """
    return json.dumps(my_obj)
