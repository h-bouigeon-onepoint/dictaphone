import unittest
import os
from services.handle_json import write_json_file
from services.get_all_json_contents import get_all_json_contents


class TestGetAllTxtContents(unittest.TestCase):
    def setUp(self):
        self.directory_path = "test_directory"
        self.file_paths = [
            "test_directory/file1.txt",
            "test_directory/file2.txt",
            "test_directory/nested_directory/file3.txt",
        ]
        self.file_contents = [
            {"You should write test to avoid surprise": ""},
            {"This is file 2 contents.": ""},
            {"This is file 3 contents.": ""},
        ]
        os.makedirs(os.path.dirname(self.file_paths[0]))
        os.makedirs(os.path.dirname(self.file_paths[2]))
        for i, file_path in enumerate(self.file_paths):
            write_json_file(file_path, self.file_contents[i])

    def tearDown(self):
        for file_path in self.file_paths:
            os.remove(file_path)
        os.removedirs(os.path.dirname(self.file_paths[2]))

    def test_get_all_json_contents(self):
        all_json_contents = get_all_json_contents(self.directory_path)
        self.assertEqual(all_json_contents, self.file_contents)


if __name__ == "__main__":
    unittest.main()
