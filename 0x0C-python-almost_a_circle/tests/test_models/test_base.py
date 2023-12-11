#!/usr/bin/python3
"""Unit tests for the Base class."""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_init_no_id(self):
        """Test if id is assigned correctly when not provided."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_init_with_id(self):
        """Test if id is assigned correctly when provided."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_increment_id(self):
        """Test if id is incremented correctly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

if __name__ == "__main__":
    unittest.main()
