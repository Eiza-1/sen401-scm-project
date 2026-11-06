"""Unit tests for students.py and utils/helpers.py.

Run with:  python -m unittest discover -s tests -v
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import students  # noqa: E402
from utils.helpers import highest_score, lowest_score, pass_count  # noqa: E402

SAMPLE = [{"name": "A", "score": 40}, {"name": "B", "score": 60}, {"name": "C", "score": 80}]


class TestEmptyList(unittest.TestCase):
    """Corrective maintenance: nothing should crash on an empty list."""

    def test_average_empty(self):
        self.assertEqual(students.average_score([]), 0)

    def test_median_empty(self):
        self.assertEqual(students.median_score([]), 0)

    def test_pass_rate_empty(self):
        self.assertEqual(students.pass_rate([]), 0.0)

    def test_highest_lowest_empty(self):
        self.assertIsNone(highest_score([]))
        self.assertIsNone(lowest_score([]))


class TestStatistics(unittest.TestCase):
    def test_average(self):
        self.assertEqual(students.average_score(SAMPLE), 60)

    def test_median_even(self):
        data = SAMPLE + [{"name": "D", "score": 100}]
        self.assertEqual(students.median_score(data), 70)

    def test_pass_rate(self):
        self.assertAlmostEqual(students.pass_rate(SAMPLE), 200 / 3)

    def test_helpers(self):
        self.assertEqual(highest_score(SAMPLE)["name"], "C")
        self.assertEqual(lowest_score(SAMPLE)["name"], "A")
        self.assertEqual(pass_count(SAMPLE), 2)


class TestValidation(unittest.TestCase):
    """Adaptive maintenance: invalid input is rejected."""

    def test_valid(self):
        self.assertEqual(students.validate_student("  Emeka ", 88), {"name": "Emeka", "score": 88})

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            students.validate_student("   ", 50)

    def test_non_numeric_score(self):
        with self.assertRaises(TypeError):
            students.validate_student("Emeka", "ninety")

    def test_bool_score(self):
        with self.assertRaises(TypeError):
            students.validate_student("Emeka", True)

    def test_out_of_range(self):
        for bad in (-1, 101):
            with self.assertRaises(ValueError):
                students.validate_student("Emeka", bad)

    def test_get_students_returns_copy(self):
        copy = students.get_students()
        copy.append({"name": "X", "score": 1})
        self.assertNotIn({"name": "X", "score": 1}, students.students)


if __name__ == "__main__":
    unittest.main()
