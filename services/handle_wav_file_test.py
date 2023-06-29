import wave
import os
import unittest
from services.handle_wav_file import WavWriter


class TestWavWriter(unittest.TestCase):
    def setUp(self):
        self.audio_file_path = "test.wav"
        self.sample_rate = 44100
        self.wav_data = b"\x00\x00\x00\x00\x00\x00\x00\x00" * 1000

    def test_wav_writer(self):
        wav_writer = WavWriter(self.audio_file_path)
        wav_writer.write_audio(self.wav_data)
        wav_writer.close()

        # check that file exists
        self.assertTrue(os.path.exists(self.audio_file_path))

        # check that file is a valid WAV file
        with wave.open(self.audio_file_path, "rb") as wav_file:
            self.assertEqual(wav_file.getnchannels(), 1)
            self.assertEqual(wav_file.getsampwidth(), 2)
            self.assertEqual(wav_file.getframerate(), self.sample_rate)
            self.assertEqual(wav_file.getnframes(), len(self.wav_data) // 2)

    def tearDown(self):
        # clean up test file
        os.remove(self.audio_file_path)


if __name__ == "__main__":
    unittest.main()
