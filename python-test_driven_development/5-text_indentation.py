#!/usr/bin/python3
"""
Module prints a text with 2 new lines after each of these characters:
., ?, and :.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each of these characters: ., ?, and :.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_characters = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in special_characters:
            result += "\n\n"

    print("\n".join([line.strip() for line in result.split("\n")]))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
