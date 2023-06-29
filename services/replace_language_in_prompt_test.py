import unittest
from services.replace_language_in_prompt import replace_language_in_prompt


class TestReplaceLanguageInPrompt(unittest.TestCase):
    def test_replace_language_in_prompt(self):
        prompt = (
            'and the deadline as follow {{"action":"action", "responsable":"name", "deadline":"date mentioned"}} '
            "Only use this format, in {language}, nothing else, be precise, synthetic and DO NOT make up subjects, avoid redundancy.\n"
            "Text: ```{text}```"
        )
        language = "english"
        expected_prompt = (
            'and the deadline as follow {{"action":"action", "responsable":"name", "deadline":"date mentioned"}} '
            "Only use this format, in english, nothing else, be precise, synthetic and DO NOT make up subjects, avoid redundancy.\n"
            "Text: ```{text}```"
        )
        result_prompt = replace_language_in_prompt(prompt, language)
        self.assertEqual(result_prompt, expected_prompt)

    def test_replace_language_in_prompt_with_braces(self):
        prompt = "Select {language} as your preferred language to continue. For more information, see {text}."
        language = "Python"
        expected_prompt = "Select Python as your preferred language to continue. For more information, see {text}."
        result_prompt = replace_language_in_prompt(prompt, language)
        self.assertEqual(result_prompt, expected_prompt)


if __name__ == "__main__":
    unittest.main()
