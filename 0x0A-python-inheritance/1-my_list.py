#!/usr/bin/python3
"""
This module defines the MyList class.
"""


class MyList(list):
    """
    The MyList class inherits from the built-in list class.

    Methods:
        print_sorted - Prints the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
