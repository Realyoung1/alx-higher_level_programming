#!/usr/bin/python3

"""Defining a Pascal's Triangle functions."""


def pascal_triangle(n):
    """Representing Pascal's Triangles of size n.
    Returns a list of lists of integers representings the triangles.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
