#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): Matrix containing integers or floats.
    div (int or float): Divisor for dividing matrix elements.

    Returns:
    list of lists: New matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               or if each row of the matrix is not of the same size,
               or if div is not a number (integer or float).
    ZeroDivisionError: If div is equal to zero.
    """

    # Validate if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate if matrix is a list of lists containing integers or floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate if each row of the matrix has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divide all elements of the matrix by div and round to 2 decimal places
    divided_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return divided_matrix
