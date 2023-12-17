import unittest
from models.base import Base
import os

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        # Test when list is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test with a list of dictionaries
        input_list = [{'id': 1, 'name': 'obj1'}, {'id': 2, 'name': 'obj2'}]
        expected_output = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

    def test_save_to_file(self):
        # Test saving to file
        dummy_instance = Base()
        dummy_instance.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))

    def test_from_json_string(self):
        # Test when input is an empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test with a valid JSON string
        json_string = '[{"id": 1, "name": "obj1"}, {"id": 2, "name": "obj2"}]'
        expected_output = [{'id': 1, 'name': 'obj1'}, {'id': 2, 'name': 'obj2'}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_create(self):
        # Test creating an instance with create method
        dummy_instance = Base.create(id=1, name="obj1")
        self.assertEqual(dummy_instance.id, 1)
        self.assertEqual(dummy_instance.name, "obj1")

    def test_load_from_file(self):
        # Test loading from file
        dummy_instance = Base()
        dummy_instance.save_to_file([])
        loaded_instances = dummy_instance.load_from_file()
        self.assertEqual(len(loaded_instances), 0)

if __name__ == '__main__':
    unittest.main()
