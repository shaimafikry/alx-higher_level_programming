#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_nonlist_test(self):
        m = []
        self.assertEqual(max_integer(m), None)

    def test_max_at_the_begining(self):
        m = [6, 2, 3]
        self.assertEqual(max_integer(m), 6)

    def test_max_at_the_end(self):
        m = [1, 2, 3]
        self.assertEqual(max_integer(m), 3)

    def test_one_negitive_exist(self):
        m = [6, -1, 3]
        self.assertEqual(max_integer(m), 6)

    def test_max_at_the_middle(self):
        m = [6, 9, 3]
        self.assertEqual(max_integer(m), 9)

    def test_only_negitive_exist(self):
        m = [-2, -3, -7]
        self.assertEqual(max_integer(m), -2)

    def test_list_of_one_elemnt(self):
        m = max_integer([6])
        self.assertEqual(m, 6)


if __name__ == '__main__':
    unittest.main()
