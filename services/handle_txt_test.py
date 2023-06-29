import unittest
import os
from services.handle_txt import read_txt_file, write_txt_file

class TestTextFileFunctions(unittest.TestCase):
    def setUp(self):
        self.text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        self.file_path = 'test.txt'

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_txt_file(self):
        write_txt_file(self.file_path, self.text)
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_txt_file(self):
        write_txt_file(self.file_path, self.text)
        read_text = read_txt_file(self.file_path)
        self.assertEqual(read_text, self.text)

if __name__ == '__main__':
    unittest.main()
