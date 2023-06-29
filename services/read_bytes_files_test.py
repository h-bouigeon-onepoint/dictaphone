import unittest
import os
from services.read_bytes_files import read_bytes_file


class TestReadBytesFile(unittest.TestCase):
    def setUp(self):
        self.file_path = "test.txt"
        self.text = b"Hello, world! This is a test."

        with open(self.file_path, "wb") as file:
            file.write(self.text)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_read_bytes_file(self):
        result = read_bytes_file(self.file_path)
        self.assertIsInstance(result, bytes)
        self.assertEqual(result, self.text)


if __name__ == "__main__":
    unittest.main()
