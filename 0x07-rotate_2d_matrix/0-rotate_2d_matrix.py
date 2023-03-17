#!/usr/bin/python3
""" rotate matrix inplace
"""


def rotate_2d_matrix(mat):
    """ rotates 2d matrix 90 degrees clockwise
    """
    N = len(mat)
    for i in range(N // 2):
        offset = 0
        x = N - i - 1
        for j in range(i, N - i - 1):
            tmp = mat[i][j]
            mat[i][j] = mat[x - offset][i]
            mat[x - offset][i] = mat[x][x - offset]
            mat[x][x - offset] = mat[j][x]
            mat[j][x] = tmp
            offset += 1
