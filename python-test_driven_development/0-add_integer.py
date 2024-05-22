#!/usr/bin/python3
"""This is a module to add two integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number, defaults to 98.

    Returns:
    int: The sum of a and b as an integer.
"""

    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
