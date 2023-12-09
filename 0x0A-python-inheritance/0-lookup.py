#!/usr/bin/python3
"""
This module defines a function for looking up available attributes and
methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods for the given object.

    Args:
        obj (object): The object for which to retrieve attributes and methods.

    Returns:
        list: A list containing the names of the attributes and methods.
    """
    return dir(obj)
