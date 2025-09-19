import unittest
from task5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")
        self.assertEqual(convert_date_format("1999-12-01"), "01-12-1999")
        self.assertEqual(convert_date_format("2023-01-05"), "05-01-2023")

    def test_invalid_format_slashes(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")

    def test_missing_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")
        with self.assertRaises(ValueError):
            convert_date_format("2023")
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_extra_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15-01")

    def test_non_numeric(self):
        # The function does not check for numeric, just splits, so this should not raise
        self.assertEqual(convert_date_format("abcd-ef-gh"), "gh-ef-abcd")

    def test_leading_zeros(self):
        self.assertEqual(convert_date_format("2023-01-09"), "09-01-2023")

if __name__ == "__main__":
    unittest.main()
