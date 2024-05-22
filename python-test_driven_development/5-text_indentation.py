#!/usr/bin/python3
"""
Module prints a text with 2 new lines.
"""


def text_indentation(text):
    """
    text_indentation prints text with two lines after charcters
    Args:
    text (str): the type of text is string
    Raises:
    TypeError: text must be a string
    Return:
    print text line per line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".").replace("?", ".").replace(":", ".")
    text = text.split(".")
    for line in text:
        result = "".join(line.strip())
        result = result.strip()
        print(result)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
