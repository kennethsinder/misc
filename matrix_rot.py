#!/usr/bin/env python
###########################
# Programmed by: Kenneth Sinder
# Date created: 2017-11-01
# Filename: matrix_rot.py
# Description: Rotate square matrices
###########################

from math import floor

def rot(M):
    """ (list of list) -> list of list
    In-place square matrix rotation. Clockwise 90 deg.
    Also returns the modified matrix for convenience.
    >>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> M = rot(M)
    >>> print(M)
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    >>> rot([])
    []
    """
    N = len(M)
    for layer in range(0, floor(N / 2)):
        last = N - 1 - layer
        for i in range(layer, last):
            offset = i - layer
            temp = M[layer][i]
            M[layer][i] = M[last - offset][layer]
            M[last - offset][layer] = M[last][last - offset]
            M[last][last - offset] = M[i][last]
            M[i][last] = temp
    return M

if __name__ == '__main__':
    import doctest
    doctest.testmod()
