import unittest
import os
from services.handle_pickle import write_pickle_file, read_pickle_file

class TestPickleFunctions(unittest.TestCase):
    def setUp(self):
        self.data = {'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}
        self.file_path = 'test.pickle'

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_write_pickle_file(self):
        write_pickle_file(self.file_path, self.data)
        self.assertTrue(os.path.exists(self.file_path))

    def test_read_pickle_file(self):
        write_pickle_file(self.file_path, self.data)
        data = read_pickle_file(self.file_path)
        self.assertEqual(data, self.data)

if __name__ == '__main__':
    unittest.main()
