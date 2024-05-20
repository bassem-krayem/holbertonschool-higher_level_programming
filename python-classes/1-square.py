#!/usr/bin/python3
# 1-square.py
"""a class Square that defines a square by: (based on 0-square.py)."""


class Square:
    """ a class names square."""
    
    def __init__(self, size):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
