#!/usr/bin/python3
"""This module defines the function `pascal_triangle`"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Parameters:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.
    """
    triangle = []
    for idx in range(n):
        row = []
        for val in range(idx + 1):
            if (val == 0) or (val == i):
                row.append(1)
            else:
                row.append(triangle[idx - 1][val] + triangle[idx - 1][val - 1])
        triangle.append(row)
    return triangle
