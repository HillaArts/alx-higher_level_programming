#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): First number to be added.
    b (int or float): Second number to be added. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
