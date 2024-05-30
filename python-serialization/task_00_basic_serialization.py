#!/usr/bin/python3
import json

"""
This module provides functions for serializing Python objects to JSON format
and saving them to a file, as well as loading JSON data from a file and
deserializing it back into Python objects. This can be useful for persisting
data between program runs or for transferring data between different parts of
a program or between different programs.
"""


def serialize_and_save_to_file(data, filename):
    """
    Serialize the provided data to JSON format and save it to a file.

    Args:
        data (any): The data to be serialized, which can be any
        Python object that is JSON serializable.
        filename (str): The name of the file where the serialized data
        will be saved.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """

        Load JSON formatted data from a file and deserialize it into a
        Python object.

    Args:
        filename (str): The name of the file from which to load the data.

    Returns:
        any: The deserialized Python object.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
