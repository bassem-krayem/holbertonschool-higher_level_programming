#!/usr/bin/python3
"""
This script defines a function to read and print the contents of a file.

The function `read_file` takes a filename as an argument,
reads the content of the file,
and prints it to the standard output.
"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints it to the standard output.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an I/O error occurs while reading the file.
    """
    # Open the file in read mode
    with open(filename, "r") as file:
        # Read the entire content of the file
        file_content = file.read()

    # Print the file content, end="" ensures no additional newline is added
    print(file_content, end="")
