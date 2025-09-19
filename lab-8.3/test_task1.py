import unittest
from task1 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("abc@gmail.com"))  # Test Case 1

    def test_multiple_at(self):
        self.assertFalse(is_valid_email("abc@@mail.com"))  # Test Case 2

    def test_no_at(self):
        self.assertFalse(is_valid_email("abcmail.com"))  # No '@'

    def test_no_dot(self):
        self.assertFalse(is_valid_email("abc@gmailcom"))  # No '.'

    def test_starts_with_dot(self):
        self.assertFalse(is_valid_email(".abc@gmail.com"))  # Starts with '.'

    def test_ends_with_dot(self):
        self.assertFalse(is_valid_email("abc@gmail.com."))  # Ends with '.'

    def test_starts_with_at(self):
        self.assertFalse(is_valid_email("@abc@gmail.com"))  # Starts with '@'

    def test_ends_with_at(self):
        self.assertFalse(is_valid_email("abc@gmail.com@"))  # Ends with '@'

    def test_valid_email_with_subdomain(self):
        self.assertTrue(is_valid_email("abc@mail.co.uk"))  # Valid with subdomain

    def test_valid_email_with_numbers(self):
        self.assertTrue(is_valid_email("user123@domain.com"))  # Valid with numbers

if __name__ == "__main__":
    unittest.main()