#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id2_none(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_value(self):
        b3 = Base(5)
        self.assertEqual(b3.id, 5)


if __name__ == "__main__":
    unittest.main()
