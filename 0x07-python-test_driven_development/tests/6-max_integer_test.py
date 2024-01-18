#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def nonlist_test(self):
        m = []
        self.assertEqual(max_integer(m), None)

    def max_at_the_begining(self):
        m = [6, 2, 3]
        self.assertEqual(max_integer(m), 6)

    def max_at_the_end(self):
        m = [1, 2, 3]
        self.assertEqual(max_integer(m), 3)

    def one_negitive_exist(self):
        m = [6, -1, 3]
        self.assertEqual(max_integer(m), 6)

    def max_at_the_middle(self):
        m = [6, 9, 3]
        self.assertEqual(max_integer(m), 9)

    def only_negitive_exist(self):
        m = [-2, -3, -7]
        self.assertEqual(max_integer(m), -2)

    def list_of_one_elemnt(self):
        m = [6]
        self.assertEqual(max_integer(m), 6)


if __name__ == '__main__':
    unittest.main()
