import os
import unittest
from services.convert_audio_to_mp3 import convert_audio_file_to_mp3


class AudioConversionTest(unittest.TestCase):
    def setUp(self):
        self.audio_file_test_path = "audio_test/joyeux_noel.mp3"
        self.output_filename = "./filename"
        self.output_path = f"{self.output_filename}.mp3"

    def test_convert_audio_file_to_mp3(self):
        convert_audio_file_to_mp3(self.audio_file_test_path, self.output_filename)
        self.assertTrue(os.path.exists(self.output_path))

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)


if __name__ == "__main__":
    unittest.main()
