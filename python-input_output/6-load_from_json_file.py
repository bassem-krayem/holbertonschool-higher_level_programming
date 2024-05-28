#!/usr/bin/python3
"""
This script defines a function to load a Python object from a JSON file.

The function `load_from_json_file` takes a filename as an argument and returns
the corresponding Python object.
"""

import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the file to load the object from.

    Returns:
        Any: The Python object corresponding to the JSON file content.

    Raises:
        IOError: If an I/O error occurs while reading the file.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    with open(filename, "r") as file:
        return json.load(file)
