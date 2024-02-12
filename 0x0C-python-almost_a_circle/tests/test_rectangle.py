#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
import json
import io
import sys


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(1, 1, 5, 5, 6)

    def test_init(self):
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 1)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 5)
        self.assertEqual(self.rectangle.id, 6)

        b = Rectangle(1, 2)
        self.assertEqual(b.width, 1)
        self.assertEqual(b.height, 2)

        with self.assertRaises(TypeError):
            b = Rectangle("1", 2)

        b = Rectangle(1, 2, 3)
        self.assertEqual(b.width, 1)
        self.assertEqual(b.height, 2)
        self.assertEqual(b.x, 3)

        b = Rectangle(1, 2, 3, 4)
        self.assertEqual(b.width, 1)
        self.assertEqual(b.height, 2)
        self.assertEqual(b.x, 3)
        self.assertEqual(b.y, 4)

        with self.assertRaises(TypeError):
            b = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            b = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            b = Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            b = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            b = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            b = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            b = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            b = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            b = Rectangle(1, 2, 3, -4)

    def test_display(self):
        captured_output = io.StringIO()  # Capture the standard output
        sys.stdout = captured_output
        rect = Rectangle(3, 4)  # Replace with the actual constructor parameters
        rect.display()
        sys.stdout = sys.__stdout__  # Restore the standard output
        output = captured_output.getvalue()  # Retrieve the captured output
        exp_result = "###\n###\n###\n###\n"
        self.assertEqual(output, exp_result)
        captured_output = io.StringIO()  # Capture the standard output
        sys.stdout = captured_output
        rect = Rectangle(1, 2, 3)  # Replace with the actual constructor parameters
        rect.display()
        sys.stdout = sys.__stdout__  # Restore the standard output
        output = captured_output.getvalue()  # Retrieve the captured output
        exp_result = "   #\n   #\n"
        self.assertEqual(output, exp_result)

        capturd_output = io.StringIO()
        sys.stdout = capturd_output
        b = Rectangle(1, 2, 3, 4)
        b.display()
        sys.stdout = sys.__stdout__
        output = capturd_output.getvalue()
        exp_result = "\n\n\n\n   #\n   #\n"
        self.assertEqual(output, exp_result)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 1)

    def test_str(self):
        result = self.rectangle.__str__()
        self.assertEqual(result, "[Rectangle] (6) 5/5 - 1/1")

    def test_update(self):
        """ using args"""
        self.rectangle.update(*(4, 6, 9, 8, 9))
        self.assertEqual(self.rectangle.id, 4)
        self.assertEqual(self.rectangle.width, 6)
        self.assertEqual(self.rectangle.height, 9)
        self.assertEqual(self.rectangle.x, 8)
        self.assertEqual(self.rectangle.y, 9)
        """using kwargs"""
        self.rectangle.update(**{"id": 2, "width": 12, "height": 8, "x": 13, "y": 5})
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 12)
        self.assertEqual(self.rectangle.height, 8)
        self.assertEqual(self.rectangle.x, 13)
        self.assertEqual(self.rectangle.y, 5)

    def test_to_dictionary(self):
        result = self.rectangle.to_dictionary()
        self.assertEqual(result, {"id": 6, "width": 1, "height": 1, "x": 5, "y": 5})

    def test_create(self):
        m = {"height": 4, "width": 10}
        inst = Rectangle.create(**m)
        self.assertIsInstance(inst, Rectangle)

    def test_save_to_file(self):
        b = Rectangle(1, 2)
        b2 = Rectangle(3, 4)
        data_list = [b, b2]
        Rectangle.save_to_file(data_list)
        with open("Rectangle.json", "r", encoding="utf-8") as fe:
            data = fe.read()
        data_compare = json.loads(data)
        for i, n in zip(data_list, data_compare):
            self.assertEqual(i.to_dictionary(), n)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as fe:
            data = fe.read()
        data_compare = json.loads(data)
        self.assertEqual([], data_compare)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as fe:
            data = fe.read()
        data_compare = json.loads(data)
        self.assertEqual([], data_compare)


    def test_load_from_file(self):
        list_inst = Rectangle.load_from_file()
        for i in list_inst:
            self.assertIsInstance(i, Rectangle)

    def test_load_from_file_not_exist(self):
        list_inst = Rectangle.load_from_file()
        self.assertEqual(list_inst, [])


if __name__ == "__main__":
    unittest.main()
