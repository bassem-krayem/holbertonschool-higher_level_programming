#!/usr/bin/python3
"""
This script adds command-line arguments to a list and saves the list to
a JSON file.

Functions:
    add_from_cmd: Collects command-line arguments into a list.
    save_to_json_file: Saves a Python object to a file in JSON format.
"""

import sys
import json


def add_from_cmd():
    """
    Adds command-line arguments to a list.

    Returns:
        list: A list containing the command-line arguments.
    """
    return sys.argv[1:]


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
        json.dump(my_obj, file)


if __name__ == "__main__":
    my_list = add_from_cmd()
    save_to_json_file(my_list, "add_item.json")
