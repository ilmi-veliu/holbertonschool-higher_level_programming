#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([0, 500, 200, -650]), 500, "Max is wrong")
        self.assertEqual(max_integer([0, 500, 200, 650]), 650, "Max is wrong")
        self.assertEqual(max_integer([650, 500, 200, -650]), 650, "Max is wrong")

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Should return None for empty list")

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -20, -3, -40]), -3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.2]), 2.7)

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == '__main__':
    unittest.main()