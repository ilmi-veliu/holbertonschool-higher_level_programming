#!/usr/bin/python3
"""
Module 12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle:
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    p_list = []
    for j in range(n):
        new_list = [1]
        if j >= 2:
            i = 1
            while i < j:
                new_list.append(p_list[j - 1][i] + p_list[j - 1][i - 1])
                i += 1
        if j >= 1:
            new_list.append(1)
        p_list.append(new_list)
    return p_list
