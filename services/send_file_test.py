import unittest
from flask import Response
from services.send_file import send_word_file, send_ppt_file


class TestFileSendingFunctions(unittest.TestCase):
    def setUp(self):
        self.file = b"This is a test file."
        self.word_file_name = "test_word_file.docx"
        self.ppt_file_name = "test_ppt_file.pptx"

    def test_send_word_file(self):
        response = send_word_file(self.file, filename=self.word_file_name)
        self.assertIsInstance(response, Response)
        self.assertEqual(
            response.mimetype,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
        self.assertEqual(
            response.headers["Content-Disposition"],
            f"attachment; filename={self.word_file_name}",
        )

    def test_send_ppt_file(self):
        response = send_ppt_file(self.file, filename=self.ppt_file_name)
        self.assertIsInstance(response, Response)
        self.assertEqual(
            response.mimetype,
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
        self.assertEqual(
            response.headers["Content-Disposition"],
            f"attachment; filename={self.ppt_file_name}",
        )


if __name__ == "__main__":
    unittest.main()
