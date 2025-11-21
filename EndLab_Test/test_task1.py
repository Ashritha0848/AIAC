import unittest
from task1 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_element_found_middle(self):
        # Sorted paired list: (value, original_index)
        arr = [(1, 0), (3, 1), (5, 2), (7, 3), (9, 4)]
        self.assertEqual(binary_search(arr, 5), 2)

    def test_element_found_start(self):
        arr = [(1, 0), (3, 1), (5, 2)]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_element_found_end(self):
        arr = [(2, 0), (4, 1), (6, 2)]
        self.assertEqual(binary_search(arr, 6), 2)

    def test_element_not_found(self):
        arr = [(10, 0), (20, 1), (30, 2)]
        self.assertEqual(binary_search(arr, 25), -1)

    def test_single_element_found(self):
        arr = [(100, 0)]
        self.assertEqual(binary_search(arr, 100), 0)

    def test_single_element_not_found(self):
        arr = [(50, 0)]
        self.assertEqual(binary_search(arr, 40), -1)

    def test_empty_list(self):
        arr = []
        self.assertEqual(binary_search(arr, 10), -1)

    def test_duplicates(self):
        # In case duplicates exist, binary search should return the correct original index for whichever match it hits
        arr = [(2, 0), (3, 1), (3, 2), (4, 3)]
        result = binary_search(arr, 3)
        self.assertIn(result, [1, 2])  # Acceptable: either duplicate

    def test_negative_numbers(self):
        arr = [(-5, 0), (-2, 1), (0, 2), (3, 3)]
        self.assertEqual(binary_search(arr, -2), 1)

    def test_float_numbers(self):
        arr = [(1.1, 0), (2.5, 1), (3.8, 2)]
        self.assertEqual(binary_search(arr, 2.5), 1)


if __name__ == "__main__":
    unittest.main()
