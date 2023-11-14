#!/usr/bin/python3
"""Defines unittests for base.py.

"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):

    def test(self):
        b1 = Base()
        print(b1.id)

        b2 = Base()
        print(b2.id)

        b3 = Base()
        print(b3.id)

        b4 = Base(12)
        print(b4.id)
        b5 = Base()
        print(b5.id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_string_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_noargs(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_list_id(self):
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_two_arg(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_floit_id(self):
        with self.assertRaises(TypeError):
            Base(1, 2.2)

    def test_None_id(self):
        with self.assertRaises(TypeError):
            Base(1, None)

    def test_ziro_id(self):
        with self.assertRaises(TypeError):
            Base(1, 0)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBase_to_json_string(unittest.TestCase):
    
    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertIs(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_square_type(self):
        t = Square(10, 2, 3, 4)
        self.assertNotEqual(str,type,(Base.to_json_string, [t.to_dictionary()]))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
            
    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) > 0 )

    def test_to_json_string_square_one_dict(self):
        t = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([t.to_dictionary()])) > 0)

    def test_to_json_string_(self):
        self.assertTrue(len(Base.to_json_string([ { 'id': 12 } ])) > 0)

    def test_json_string_str_(self):
        self.assertTrue(isinstance(Base.to_json_string([ { 'id': 12 } ]), str))
    
    def test_json_string(self):
        self.assertTrue(Base.from_json_string('[{ "id": 89 }]'))

class TestBase_save_to_file(unittest.TestCase):

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
class TestBase_from_json_string(unittest.TestCase):
    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)
class TestBase_create(unittest.TestCase):

    def test_create_with_squre(self):
        square_dict = {'id': 89, 'size': 1}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)

    def test__create_with_id(self):
        square_dict = {'id': 89, 'size': 1}
        square = Square.create(**square_dict)
        self.assertEqual(square.id, 89)

    def test__create_with_size(self):
        square_dict = {'id': 89, 'size': 1}
        square = Square.create(**square_dict)
        self.assertEqual(square.size, 1)

    def test_create_squear(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)

    def test_create_id(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2}
        created_square = Square.create(**square_dict)
        self.assertEqual(created_square.id, 89)

    def test_create_cd_size(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2}
        square = Square.create(**square_dict)
        self.assertEqual(square.size, 1)

    def test_create_x(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2}
        square = Square.create(**square_dict)
        self.assertEqual(square.x, 2)

    def test_create_with_size_x_and_y(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        created_square = Square.create(**square_dict)
        self.assertIsInstance(created_square, Square)
    def test_create_y(self):
        square_dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        square = Square.create(**square_dict)
        self.assertEqual(square.y, 3)
if __name__ == '__main__':
    unittest.main()
    