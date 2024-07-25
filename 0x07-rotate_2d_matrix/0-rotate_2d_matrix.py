#!/usr/bin/ python3

"""
module: 0-rotate_2d_matrix

holds one function: rotate_2d_matrix(matrix)
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90 degrees in-place.

    Parameters:
        matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
        None

    Example:
        >>> matrix = [[1, 2, 3],
        ...           [4, 5, 6],
        ...           [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> matrix
        [[3, 6, 9],
         [2, 5, 8],
         [1, 4, 7]]
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
