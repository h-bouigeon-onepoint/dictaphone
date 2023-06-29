import unittest
import os
from services.handle_json import read_json_file, write_json_file


class TestdictionaryFileFunctions(unittest.TestCase):
    def setUp(self):
        self.dictionary = {"actions": [{"action1": "MAKE UNIT TESTS :)"}]}
        self.file_path = "test.json"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_json_file(self):
        write_json_file(self.file_path, self.dictionary)
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_json_file(self):
        write_json_file(self.file_path, self.dictionary)
        read_dictionary = read_json_file(self.file_path)
        self.assertEqual(read_dictionary, self.dictionary)


if __name__ == "__main__":
    unittest.main()
