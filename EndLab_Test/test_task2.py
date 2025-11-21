import unittest
from task2 import validate_password


class TestValidatePassword(unittest.TestCase):

    # -------- VALID PASSWORDS --------
    def test_valid_passwords(self):
        valid_passwords = [
            "Abcdef1!",
            "Password1@",
            "Xyz12345#",
            "LONGpass9$",
            "A1aaaaaa!",
            "MixEdCASE9@"
        ]
        for pwd in valid_passwords:
            with self.subTest(pwd=pwd):
                self.assertTrue(validate_password(pwd))

    # -------- TOO SHORT --------
    def test_too_short_passwords(self):
        short_passwords = [
            "Ab1!",
            "A1!aaaa",
            "",
            "Abc1!"
        ]
        for pwd in short_passwords:
            with self.subTest(pwd=pwd):
                self.assertFalse(validate_password(pwd))

    # -------- MISSING DIGIT --------
    def test_missing_digit(self):
        passwords = [
            "Abcdefgh!",
            "NoDigits!!"
        ]
        for pwd in passwords:
            with self.subTest(pwd=pwd):
                self.assertFalse(validate_password(pwd))

    # -------- MISSING UPPERCASE --------
    def test_missing_uppercase(self):
        passwords = [
            "abcdefg1!",
            "lowercase1@"
        ]
        for pwd in passwords:
            with self.subTest(pwd=pwd):
                self.assertFalse(validate_password(pwd))

    # -------- MISSING SPECIAL CHAR --------
    def test_missing_special_character(self):
        passwords = [
            "Abcdef12",
            "A1bcdefgH"
        ]
        for pwd in passwords:
            with self.subTest(pwd=pwd):
                self.assertFalse(validate_password(pwd))

    # -------- DISALLOWED SPECIAL CHAR --------
    def test_disallowed_special(self):
        passwords = [
            "Abcdef1%",
            "Passw0rd&",
            "Abcde1^"
        ]
        for pwd in passwords:
            with self.subTest(pwd=pwd):
                self.assertFalse(validate_password(pwd))

    # -------- NON-STRING INPUTS --------
    def test_non_string_inputs(self):
        inputs = [
            None,
            12345678,
            12.34,
            b"Abcdef1!",
            ["A", "b", "1", "!"]
        ]
        for pwd in inputs:
            with self.subTest(pwd=pwd):
                self.assertFalse(validate_password(pwd))

    # -------- COMPLEX VALID PASSWORD --------
    def test_complex_valid_password(self):
        pwd = "ThisIsAValidPassword123!@#"
        self.assertTrue(validate_password(pwd))


# Run the tests
if __name__ == "__main__":
    unittest.main()
