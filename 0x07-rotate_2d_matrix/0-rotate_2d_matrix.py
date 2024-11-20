#!/usr/bin/python3
"""This module contains a function that rotates an n x n 2D matrix
   90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """function that rotates an n x n
    2D matrix by 90 degrees clockwise.
    """
    i, j = len(matrix), len(matrix[0])
    for a in range(i):
        for b in range(j):
            if b > a:
                temp = matrix[a][b]
                matrix[a][b] = matrix[b][a]
                matrix[b][a] = temp
    for a in range(i):
        y, z = 0, len(matrix[0]) - 1
        while y < z:
            temp = matrix[a][y]
            matrix[a][y] = matrix[a][z]
            matrix[a][z] = temp
            y += 1
            z -= 1
