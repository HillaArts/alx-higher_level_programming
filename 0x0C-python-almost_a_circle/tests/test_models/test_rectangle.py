import unittest
from models.rectangle import Rectangle
import os

class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_attributes(self):
        # Test Rectangle attributes
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)

    def test_to_dictionary(self):
        # Test to_dictionary method
        r = Rectangle(10, 7, 2, 8)
        r_dict = r.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        self.assertEqual(r_dict, expected_dict)

    def test_update(self):
        # Test update method
        r = Rectangle(10, 7, 2, 8)
        r.update(2, 4, 6, 8, 10)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 10)

    def test_save_to_file(self):
        # Test saving to file
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

if __name__ == '__main__':
    unittest.main()
