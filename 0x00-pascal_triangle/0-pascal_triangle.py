#!/usr/bin/python3
"""Creating a function for the Pascal's Triangle"""


def pascal_triangle(n):
    """it returns a lists thats of integers thats representing
    the Pascal’s p_triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous = triangle[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        triangle.append(current)
    return triangle
