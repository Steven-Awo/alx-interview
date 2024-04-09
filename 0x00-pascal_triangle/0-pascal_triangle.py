#!/usr/bin/python3
"""Creating a function for the Pascal's Triangle"""

def pascal_triangle(nunb):
    """
    it returns a lists thats of integers
    thats representing the Pascal’s p_triangle
    """
    if nunb <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != nunb:
        prev = triangle[-1]
        currnt = [1]
        for x in range(len(prev) - 1):
            currnt.append(prev[x] + prev[x + 1])
        currnt.append(1)
        triangle.append(currnt)
    return triangle
