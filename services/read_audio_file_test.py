import unittest
import io
import os
from services.read_audio_file import read_audio_file

class TestAudioFunctions(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test.wav'
        with open(self.file_path, 'wb') as f:
            f.write(b'12345')

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_read_audio_file(self):
        file = read_audio_file(self.file_path)
        self.assertIsInstance(file, io.BufferedReader)
        contents = file.read()
        self.assertEqual(contents, b'12345')

if __name__ == '__main__':
    unittest.main()
