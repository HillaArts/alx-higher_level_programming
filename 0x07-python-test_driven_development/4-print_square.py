#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters of a given size.

    Args:
    size (int): Size length of the square to be printed.

    Returns:
    None

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print('#' * size)
