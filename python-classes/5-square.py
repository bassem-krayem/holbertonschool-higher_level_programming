#!/usr/bin/python3
# 4-square.py
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
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

            Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
