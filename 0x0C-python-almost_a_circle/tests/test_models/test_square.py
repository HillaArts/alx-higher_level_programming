import unittest
from models.square import Square
import os

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_attributes(self):
        # Test Square attributes
        s = Square(5, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        # Test to_dictionary method
        s = Square(5, 2, 3)
        s_dict = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s_dict, expected_dict)

    def test_update(self):
        # Test update method
        s = Square(5, 2, 3)
        s.update(2, 4, 6, 8)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 8)

    def test_save_to_file(self):
        # Test saving to file
        s1 = Square(5, 2, 3)
        s2 = Square(3, 6, 8)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.exists("Square.json"))

if __name__ == '__main__':
    unittest.main()
