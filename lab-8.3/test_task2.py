import unittest
from task2 import assign_grade
class TestAssignGrade(unittest.TestCase):
    def test_valid_integer_input(self):
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(55), "F")
    def test_valid_float_input(self):
        self.assertEqual(assign_grade(92.5), "A")
        self.assertEqual(assign_grade(82.5), "B")
        self.assertEqual(assign_grade(72.0), "C")
        self.assertEqual(assign_grade(60.0), "D")
        self.assertEqual(assign_grade(59.9), "F")
    def test_boundary_cases(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(100), "A")
    def test_out_of_range(self):
        self.assertEqual(assign_grade(110), "Invalid input")
        self.assertEqual(assign_grade(-5), "Invalid input")
        self.assertEqual(assign_grade(100.1), "Invalid input")
        self.assertEqual(assign_grade(-0.1), "Invalid input")
    def test_non_numeric_input(self):
        self.assertEqual(assign_grade("hello"), "Invalid input")
        self.assertEqual(assign_grade(None), "Invalid input")
        self.assertEqual(assign_grade([90]), "Invalid input")
        self.assertEqual(assign_grade({}), "Invalid input")
if __name__ == "__main__":
    unittest.main()
