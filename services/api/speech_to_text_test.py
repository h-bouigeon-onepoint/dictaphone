import os
import unittest
import pandas as pd
from unittest.mock import patch
from services.handle_wav_file import WavWriter
from services.api.speech_to_text import speech_to_text


class TestSpeechToText(unittest.TestCase):
    def setUp(self):
        self.dummy_audio_file_path = "test_audio.wav"
        self.dummy_audio_file_text = "You"
        self.dummy_audio_wav_data = b"\x00\x00\x00\x00\x00\x00\x00\x00" * 5000
        self.audio_file_test_path = "audio_test/joyeux_noel.mp3"
        self.audio_file_test_text = "Ho ho ho! Joyeux Noël!"
        self.openai_api_mock_response = pd.Series({"text": self.audio_file_test_text})

    def tearDown(self):
        if os.path.exists(self.dummy_audio_file_path):
            os.remove(self.dummy_audio_file_path)

    def test_speech_to_text(self):
        # patch the api to avoid multiple billed calls
        with patch(
            "openai.Audio.transcribe", return_value=self.openai_api_mock_response
        ):
            result = speech_to_text(self.audio_file_test_path)
            self.assertEqual(result, self.audio_file_test_text)

    def test_speech_to_text_dummy_file(self):
        # Create a dummy audio file for testing
        wav_writer = WavWriter(self.dummy_audio_file_path)
        wav_writer.write_audio(self.dummy_audio_wav_data)
        wav_writer.close()

        # Call the speech_to_text function with the dummy audio file
        transcript = speech_to_text(self.dummy_audio_file_path)

        # Check that the transcript is a string and is not empty
        self.assertIsInstance(transcript, str)
        self.assertNotEqual(transcript, "")
        # self.assertEqual(transcript, self.dummy_audio_file_text)


if __name__ == "__main__":
    unittest.main()
