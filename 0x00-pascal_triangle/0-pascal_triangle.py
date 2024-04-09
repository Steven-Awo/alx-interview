#!/usr/bin/python3
"""Creating a function for the Pascal's Triangle"""

def pascal_triangle(nunb):
    """
    it returns a lists thats of integers
    thats representing the Pascal’s p_triangle
    """
    if nunb <= 0:
        return []

    p_triangle = [[1]]
    while len(p_triangle) != nunb:
        prev = p_triangle[-1]
        currnt = [1]
        for x in range(len(prev) - 1):
            currnt.append(prev[x] + prev[x + 1])
        currnt.append(1)
        p_triangle.append(currnt)
    return p_triangle
