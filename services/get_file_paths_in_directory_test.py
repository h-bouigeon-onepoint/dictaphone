import unittest
import os
from services.get_file_paths_in_directory import get_file_paths, get_full_file_paths


class TestFileFunctions(unittest.TestCase):
    def setUp(self):
        self.test_directories = ["test_dir"]
        for directory in self.test_directories:
            os.mkdir(directory)
            with open(os.path.join(directory, "file1.txt"), "w") as f:
                f.write("test file 1")
            with open(os.path.join(directory, "file2.txt"), "w") as f:
                f.write("test file 2")
            sub_dir = os.path.join(directory, "sub_dir")
            os.mkdir(sub_dir)
            with open(os.path.join(sub_dir, "file3.txt"), "w") as f:
                f.write("test file 3")

    def tearDown(self):
        for directory in self.test_directories:
            os.remove(os.path.join(directory, "file1.txt"))
            os.remove(os.path.join(directory, "file2.txt"))
            os.remove(os.path.join(directory, "sub_dir", "file3.txt"))
            os.rmdir(os.path.join(directory, "sub_dir"))
            os.rmdir(directory)

    def test_get_file_paths(self):
        file_paths = get_file_paths(self.test_directories)
        expected_paths = ["file1.txt", "file2.txt", "sub_dir"]
        self.assertEqual(file_paths, expected_paths)

    def test_get_full_file_paths(self):
        file_paths = get_full_file_paths(self.test_directories[0])
        expected_paths = [
            os.path.join(self.test_directories[0], "file1.txt"),
            os.path.join(self.test_directories[0], "file2.txt"),
            os.path.join(self.test_directories[0], "sub_dir", "file3.txt"),
        ]
        self.assertEqual(file_paths, expected_paths)


if __name__ == "__main__":
    unittest.main()
