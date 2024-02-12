#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_value(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_to_json_string(self):
        b = [{"id": 6, "size": 7}]
        self.assertEqual(Base.to_json_string(b), '[{"id": 6, "size": 7}]')

    def test_to_json_string_exist(self):
        b = [{"id": 6}]
        self.assertEqual(Base.to_json_string(b), '[{"id": 6}]')


    def test_from_json_string_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        b = '{"id": 5, "size": 6}'
        self.assertEqual(Base.from_json_string(b), {"id": 5, "size": 6})


if __name__ == "__main__":
    unittest.main()
