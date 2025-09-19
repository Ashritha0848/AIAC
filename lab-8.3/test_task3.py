import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("madam"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_sentence_palindrome("nurses run"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama"))

    def test_not_a_palindrome(self):
        self.assertFalse(is_sentence_palindrome("hello world"))

    def test_single_character(self):
        self.assertTrue(is_sentence_palindrome("x"))

    def test_empty_string(self):
        self.assertTrue(is_sentence_palindrome(""))

    def test_mixed_case_palindrome(self):
        self.assertTrue(is_sentence_palindrome("RaceCar"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertFalse(is_sentence_palindrome("12345"))

    def test_palindrome_with_symbols_and_spaces(self):
        self.assertTrue(is_sentence_palindrome("!@# 1221 #@!"))

    def test_non_palindrome_with_punctuation(self):
        self.assertFalse(is_sentence_palindrome("This is not a palindrome!"))

if __name__ == "__main__":
    unittest.main()
