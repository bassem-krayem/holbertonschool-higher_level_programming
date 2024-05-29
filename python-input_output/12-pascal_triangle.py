#!/usr/bin/python3
""" a module that prints a triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle
    of n.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists of integers
        representing Pascal’s triangle.
                         Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)

    return triangle
