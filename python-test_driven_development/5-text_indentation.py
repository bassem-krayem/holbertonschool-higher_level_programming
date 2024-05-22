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
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in special_characters:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
