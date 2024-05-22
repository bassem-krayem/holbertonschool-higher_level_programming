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

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
