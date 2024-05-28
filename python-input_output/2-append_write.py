#!/usr/bin/python3
"""
This script defines a function to append text to a file.

The function `append_write` takes a filename and text as arguments, appends
the text to the end of the file, and returns the length of the text appended.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file and returns the number of
    characters appended.

    Args:
        filename (str): The name of the file to append to. Defaults to an
                        empty string.
        text (str): The text to append to the file. Defaults to an empty
                    string.

    Returns:
        int: The number of characters appended to the file.

    Raises:
        IOError: If an I/O error occurs while appending to the file.
    """
    with open(filename, "a") as file:
        # Append the text to the file
        data = file.write(text)
        # Return the length of the text appended
        return len(text)
