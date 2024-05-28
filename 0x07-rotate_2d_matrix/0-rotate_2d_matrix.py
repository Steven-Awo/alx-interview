#!/usr/bin/python3
"""
A function that Rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    the fuction ssetup that rotates a 2D matrix by
    90 degrees in a clockwise direction.
    """
    for r in range(int(len(matrix) / 2)):
        for c in range(r, (len(matrix) - r - 1)):
            m = (len(matrix) - 1 - c)
            tempr = matrix[r][c]

            matrix[r][c] = matrix[m][r]

            matrix[m][r] = matrix[(len(matrix) - r - 1)][m]

            matrix[(len(matrix) - r - 1)][m] = matrix[c][(len(matrix) - r - 1)]

            matrix[c][(len(matrix) - r - 1)] = tempr
