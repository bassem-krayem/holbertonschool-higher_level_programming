#!/usr/bin/python3
# 2-square.py
"""Define a class Square.

This module contains the definition of the Square class.
"""


class Square:
    """A class to represent a square.

    Attributes:
        __size (int): The size of the square. Default is 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
