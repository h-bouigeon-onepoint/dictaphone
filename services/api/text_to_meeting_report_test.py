import unittest
from unittest.mock import patch
from services.api.text_to_meeting_report import text_to_meeting_report


class TestTextToMeetingReport(unittest.TestCase):
    def setUp(self):
        self.text = "ChatGPT is not human, it is a robot."
        self.prompt = "Can you summarize this text:\n{text}"
        self.response = """{"title_meeting": "ChatGPT is not human","participants": [],"agenda": [],"elements_discussed": [],"action_to_be_taken": [],"notes": "The meeting was about the fact that ChatGPT is a robot and not a human."}"""
        self.openai_api_mock_response = {
            "choices": [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "message": {
                        "content": self.response,
                        "role": "assistant",
                    },
                }
            ],
            "created": 1682871773,
            "id": "chatcmpl-7B4737ir96XZe5w4JKyk297xtxqnk",
            "model": "gpt-3.5-turbo-0301",
            "object": "chat.completion",
            "usage": {
                "completion_tokens": 233,
                "prompt_tokens": 22,
                "total_tokens": 255,
            },
        }

    def test_text_to_meeting_report_type(self):
        meeting_report = text_to_meeting_report(self.text, self.prompt)
        self.assertIsInstance(meeting_report, dict)
        self.assertNotEqual(meeting_report, "")


if __name__ == "__main__":
    unittest.main()
