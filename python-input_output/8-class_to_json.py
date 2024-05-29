#!/usr/bin/python3
"""
This module defines a function class_to_json that returns the dictionary
description with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all the
        serializable attributes of the obj instance.
    """
    # The __dict__ attribute of an object contains all its instance variables
    # and their values as a dictionary.
    return obj.__dict__
