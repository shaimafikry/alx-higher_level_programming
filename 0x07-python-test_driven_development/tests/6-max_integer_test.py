#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def nonlist_test (self):
        m = max_integer([])
        self.assertEqual(m, None)

    def pass_test(self):
        m = max_integer([1, 2, 3])
        self.assertEqual(m, 3)
