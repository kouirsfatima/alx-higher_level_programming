#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

# Suite test for max_integer function
class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([10, -1, 20, 30]), 30)

    def test_max_float(self):
        self.assertEqual(max_integer([60, 80, 90, 12]), 90)

    def test_max_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_char(self):
        self.assertEqual(max_integer(['a', 'c']), 'c')

    def test_max_negative(self):
        self.assertEqual(max_integer([-2, -1, -3]), -1)

    def test_max_correct(self):
        self.assertEqual(max_integer([10, 10, 10]), 10)

    def test_max_zero(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_tuple(self):
        self.assertEqual(max_integer((1, 2, 3, 34)), 34)

    def test_max_list(self):
        self.assertEqual(max_integer([1, 2, 3, 34]), 34)
