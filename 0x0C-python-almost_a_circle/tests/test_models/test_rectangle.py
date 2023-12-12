#!/usr/bin/python3
"""Unit tests for the Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_init(self):
        """Test if the constructor initializes attributes correctly."""
        r = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 1)

    def test_getters_and_setters(self):
        """Test if getters and setters work as expected."""
        r = Rectangle(5, 5)
        r.width = 10
        r.height = 20
        r.x = 3
        r.y = 4
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)


if __name__ == "__main__":
    unittest.main()
