#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""

    def test_max_integer(self):
        self.assertEqual(max_integer([9, 5, 1, 7, 5, 3, 8, 5, 2, 4, 5, 6]), 9)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_sorted(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.11, 2.22, 3.33, 4.44]), 4.44)

    def test_string(self):
        self.assertEqual(max_integer("qwertyuiop"), "y")

    def test_string_nums(self):
        self.assertEqual(max_integer("36902580147"), "9")


if __name__ == '__main__':
    unittest.main()
