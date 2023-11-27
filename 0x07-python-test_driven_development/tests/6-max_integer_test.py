import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer(self):
        # Test with a list of positive integers
        result = max_integer([1, 3, 5, 7, 9])
        self.assertEqual(result, 9)

        # Test with a list of negative integers
        result = max_integer([-1, -3, -5, -7, -9])
        self.assertEqual(result, -1)

        # Test with a list containing both positive and negative integers
        result = max_integer([-1, 3, -5, 7, -9])
        self.assertEqual(result, 7)

        # Test with a list containing duplicate elements
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

        # Test with a list containing a single element
        result = max_integer([42])
        self.assertEqual(result, 42)

        # Test with a large list
        result = max_integer(list(range(1000000)))
        self.assertEqual(result, 999999)

if __name__ == '__main__':
    unittest.main()
