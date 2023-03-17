#!/usr/bin/python3
"""Test 0x07  Rotate2D matrix
"""

rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix


if __name__ == "__main__":
    mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    rotate_2d_matrix(mat)
    print(mat)
