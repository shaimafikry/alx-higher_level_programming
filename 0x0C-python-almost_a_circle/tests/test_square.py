#!/usr/bin/python3
import unittest
from models.square import Square
import json
import io
import sys


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(1, 5, 5, 6)

    def test_init(self):
        self.assertEqual(self.square.width, 1)
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 5)
        self.assertEqual(self.square.id, 6)

        b = Square(1)
        self.assertEqual(b.size, 1)

        with self.assertRaises(TypeError):
            b = Square("1")

        b = Square(1, 3)
        self.assertEqual(b.size, 1)
        self.assertEqual(b.x, 3)

        b = Square(1, 3, 4)
        self.assertEqual(b.size, 1)
        self.assertEqual(b.x, 3)
        self.assertEqual(b.y, 4)

        with self.assertRaises(TypeError):
            b = Square(1, "2")

        with self.assertRaises(TypeError):
            b = Square(1, 2, "4")

        with self.assertRaises(ValueError):
            b = Square(-1)

        with self.assertRaises(ValueError):
            b = Square(1, -2)

        with self.assertRaises(ValueError):
            b = Square(0)

        with self.assertRaises(ValueError):
            b = Square(1, 2, -3)

    def test_area(self):
        self.assertEqual(self.square.area(), 1)

    def test_str(self):
        result = self.square.__str__()
        self.assertEqual(result, "[Square] (6) 5/5 - 1")

    def test_update(self):
        """ using args"""
        self.square.update(*(4, 6, 8, 9))
        self.assertEqual(self.square.id, 4)
        self.assertEqual(self.square.size, 6)
        self.assertEqual(self.square.x, 8)
        self.assertEqual(self.square.y, 9)
        """using kwargs"""
        self.square.update(**{"id": 2, "size": 12, "x": 13, "y": 5})
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 12)
        self.assertEqual(self.square.x, 13)
        self.assertEqual(self.square.y, 5)

    def test_to_dictionary(self):
        result = self.square.to_dictionary()
        self.assertEqual(result, {"id": 6, "size": 1, "x": 5, "y": 5})

    def test_create(self):
        m = {"size": 10}
        inst = Square.create(**m)
        self.assertIsInstance(inst, Square)

    def test_save_to_file(self):
        b = Square(1)
        b2 = Square(3)
        data_list = [b, b2]
        Square.save_to_file(data_list)
        with open("Rectangle.json", "r", encoding="utf-8") as fe:
            data = fe.read()
        data_compare = json.loads(data)
        for i, n in zip(data_list, data_compare):
            self.assertEqual(i.to_dictionary(), n)

        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as fe:
            data = fe.read()
        data_compare = json.loads(data)
        for i, n in zip(data_list, data_compare):
            self.assertEqual(i.to_dictionary(), n)

        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as fe:
            data = fe.read()
        data_compare = json.loads(data)
        for i, n in zip(data_list, data_compare):
            self.assertEqual(i.to_dictionary(), n)

    def test_load_from_file(self):
        pass


if __name__ == "__main__":
    unittest.main()
