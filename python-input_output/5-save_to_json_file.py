#!/usr/bin/python3
"""
This script defines a function to save a Python object to a file
in JSON format.

The function `save_to_json_file` takes a Python object and a filename as
arguments,
and writes the JSON representation of the object to the specified file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file to save the object to.

    Raises:
        IOError: If an I/O error occurs while writing to the file.
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
