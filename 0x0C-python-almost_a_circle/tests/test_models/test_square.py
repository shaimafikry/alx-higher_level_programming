#!/usr/bin/python3
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.square = Square(1, 5, 5, 6)

    def test_init(self):
        self.assertEqual(self.square.size, 1)
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 5)
        self.assertEqual(self.square.id, 6)

    def test_area(self):
        self.assertEqual(self.square.area(), 1)

    def test_str(self):
        result = self.square.__str__()
        self.assertEquals(result, "[Square] (6) 5/5 - 1")

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


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
