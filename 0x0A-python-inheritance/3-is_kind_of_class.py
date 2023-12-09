#!/usr/bin/python3
"""
This module defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if obj is an instance of the specified class or its
        subclass; otherwise, False.
    """
    return isinstance(obj, a_class)
