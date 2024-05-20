#!/usr/bin/python3
# 6-square.py
"""Define a class Square.

This module contains the definition of the Square class.
"""


class Square:
    """A class to represent a square.

    Attributes:
        __size (int): The size of the square. Default is 0.
        __position (tuple): The position to
        start printing the square. Default is (0, 0).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with a given size and position.

        Args:
            size (int): The size of the square. Default is 0.
            position (tuple): The position to
            start printing the square. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer
            or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position to start printing the square.

        Returns:
            tuple: The position to start printing the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position to start printing the square with validation.

        Args:
            value (tuple): The new position to start printing the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

        Prints an empty line if size is 0. Uses position to offset the square.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
