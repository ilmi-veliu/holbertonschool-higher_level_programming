#!/usr/bin/python3
"""
Divides all elements of a matrix by a number.

Validates the matrix structure, checks types and dimensions,
and ensures the divisor is a proper number (not zero, NaN or infinity).
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a number, rounded to 2 decimals.

    Args:
        matrix: List of lists of integers or floats.
        div: Number (int or float) to divide by.

    Returns:
        A new matrix with the results rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is invalid or div is not a valid number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lengths = [len(row) for row in matrix]
    if row_lengths.count(row_lengths[0]) != len(row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or div != div or abs(div) == float('inf'):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
