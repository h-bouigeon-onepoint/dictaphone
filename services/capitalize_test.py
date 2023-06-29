import unittest
from services.capitalize import capitalize_first_letter


class TestCapitalizeFirstLetter(unittest.TestCase):
    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize_first_letter("hello"), "Hello")
        self.assertEqual(capitalize_first_letter("world"), "World")
        self.assertEqual(capitalize_first_letter("123"), "123")
        self.assertEqual(capitalize_first_letter(""), "")


if __name__ == "__main__":
    unittest.main()
