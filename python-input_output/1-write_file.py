#!/usr/bin/python3
"""
This script defines a function to write text to a file.

The function `write_file` takes a filename and text as arguments,
writes the text to the file, and returns the length of the text written.
"""


def write_file(filename="", text=""):
    """
    Writes the given text to the specified file.

    Args:
        filename (str): The name of the file to write to. Defaults to an
                        empty string.
        text (str): The text to write to the file. Defaults to an empty
                    string.

    Returns:
        int: The length of the text written to the file.

    Raises:
        IOError: If an I/O error occurs while writing to the file.
    """
    with open(filename, "w") as file:
        data = file.write(text)
        return len(text)
