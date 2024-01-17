#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def nonlist_test (self):
        m = max_integer([])
        self.assertEqual(m, None)

    def  max_at_the_begining(self):
        m = max_integer([6, 2, 3])
        self.assertEqual(m, 6)
    def max_at_the_end (self):
        m = max_integer([1, 2, 3])
        self.assertEqual(m, 3)
    def one_negitive_exist(self):
        m = max_integer([6, -1, 3])
        self.assertEqual(m, 6)
    def  max_at_the_middle(self):
        m = max_integer([6, 9, 3])
        self.assertEqual(m, 9)
    def only_negitive_exist(self):
        m = max_integer([-2, -3, -7])
        self.assertEqual(m, -2)
    def list_of_one_elemnt(self):
        m = max_integer([6])
        self.assertEqual(m, 6)