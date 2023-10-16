#!/usr/bin/python3
"""Defines unittests for base.py.

"""

import unittest
from unittest.mock import patch
from io import StringIO 
from models.rectangle import Rectangle

class TestRectangleInstantiation(unittest.TestCase):

    def test(self):
        r1 = Rectangle(10, 2)
        print(r1.id)

        r2 = Rectangle(2, 10)
        print(r2.id)

        r3 = Rectangle(10, 2, 0, 0, 12)
        print(r3.id)

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle(5.5, 10)


    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle("hello")

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)


    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_two_args(self):
        r1 = Rectangle(12, 2)
        r2 = Rectangle(2, 12)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
class TestRectangle_width(unittest.TestCase):
    def test_three_args(self):
        r1 = Rectangle(3, 3, 4)
        r2 = Rectangle(4, 4, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle(5.5, 10)

    def test_two_args(self):
        r1 = Rectangle(13, 1)
        r2 = Rectangle(1, 13)
        self.assertEqual(r1.id, r2.id - 1)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 0)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle("hello")

    def test_list(self):
         with self.assertRaises(TypeError):
            Rectangle([5],7)

    def test_dic(self):
        with self.assertRaises(TypeError):
            Rectangle({5,6,7},9)

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 9)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)
class TestRectangle_height(unittest.TestCase):

    def test_three_args(self):
        r1 = Rectangle(3, 3, 4)
        r2 = Rectangle(4, 4, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5.5)

    def test_two_args(self):
        r1 = Rectangle(13, 1)
        r2 = Rectangle(1, 13)
        self.assertEqual(r1.id, r2.id - 1)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle("hello")

    def test_list(self):
         with self.assertRaises(TypeError):
            Rectangle(7, [5])

    def test_dic(self):
        with self.assertRaises(TypeError):
            Rectangle(9, {5,6,7})

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(9, None)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)
class TestRectangle_x(unittest.TestCase):
    def test_three_args(self):
        r1 = Rectangle(3, 3, 4)
        r2 = Rectangle(4, 4, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_float(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 11, 5.5)

    def test_two_args(self):
        r1 = Rectangle(13, 1)
        r2 = Rectangle(1, 13)
        self.assertEqual(r1.id, r2.id - 1)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -2, 0)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle("hello")

    def test_list(self):
         with self.assertRaises(TypeError):
            Rectangle(7, 8, [5])

    def test_dic(self):
        with self.assertRaises(TypeError):
            Rectangle(9,10, {5,6,7})

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(9,11, None)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 6, -1)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, True)
class TestRectangle_y(unittest.TestCase):

    def test_three_args(self):
        r1 = Rectangle(3, 3, 4)
        r2 = Rectangle(4, 4, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, -2, -3,  0)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_string(self):
        with self.assertRaises(TypeError):
            Rectangle("hello")

    def test_list(self):
         with self.assertRaises(TypeError):
            Rectangle(7, 8, 9,  [5])

    def test_dic(self):
        with self.assertRaises(TypeError):
            Rectangle(9,10, 11, {5,6,7})

    def test_None(self):
        with self.assertRaises(TypeError):
            Rectangle(9,11, 13, None)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 6, 12,  -1)

    def test_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4,  True)
class TestRectangle_possition(unittest.TestCase):
    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_height_before_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, "invalid x")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid x", 4, "invalid width")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 4, "invalid y")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid y", 4, "invalid width")
class TestRectangle_area(unittest.TestCase):
    def test_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)
    
    def test_zero(self):
        with self.assertRaises(ValueError, msg="area must be > 0"):
            Rectangle(5, 0)

    def test_one_arg_area(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
        
    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_smal_area(self):
        r1 = Rectangle(5, 2,1)
        self.assertEqual(r1.area(), 10)

    def test_area(self):
        r1 = Rectangle(5, 5)
        self.assertNotEqual(r1.area(), 10)

    def test_area_long(self):
        r1 = Rectangle(100000,2000)
        self.assertEqual(r1.area(), 200000000)
class TestRectangleDisplay(unittest.TestCase):

    def test_display_width_height(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Rectangle(2, 3, 0, 0, 0).display
            self.assertNotEqual("##\n##\n##\n",op.getvalue())

    def test_display_width_height_x(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Rectangle(3, 3, 1, 0, 1).display
        self.assertNotEqual(" ###\n ###\n", op.getvalue())

    def test_display_width_height_y(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Rectangle(2, 5, 0, 1, 0).display
            self.assertNotEqual("\n####\          ####\n####\n####\n####\n", op.getvalue())

    def test_display_width_height_x_y(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Rectangle(2, 6, 3, 2, 0).display
            self.assertNotEqual("\n\n   ##\n   ##\n   ##\n   ##\n", op.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)

class TestRectangleStr(unittest.TestCase):
    def test_str_width_height(self):
        with patch('sys.stdout', new=StringIO()) as op:
            r = Rectangle(4, 6)
        correct_output = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertNotEqual(correct_output, op.getvalue())

    def test_str_height_width(self):
        r = Rectangle(5, 1)
        correct_output = "[Rectangle] ({}) 0/0 - 5/1".format(r.id)
        self.assertEqual(correct_output, r.__str__())

    def test_str_height_width_y(self):
        r = Rectangle(4, 6, 1)
        correct_output = "[Rectangle] ({}) 1/0 - 4/6".format(r.id)
        self.assertEqual(correct_output, r.__str__())

    def test_str_height_width_x(self):
        r = Rectangle(1, 5, 5)
        correct_output = "[Rectangle] ({}) 5/0 - 1/5".format(r.id)
        self.assertEqual(correct_output, r.__str__())
    
    def test_str_method_two_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1/2)

    def test_str_method_zoro(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(0)

    def test_str_method_oneargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)
    
    def test_str_method_negative(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(-5)
            
class TestRectangle_update_args(unittest.TestCase):
    def test_update_args_ziro_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", r. __str__())

    def test_update_args_one_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", r. __str__())

    def test_update_two_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", r. __str__())

    def test_update_tree_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", r. __str__())

    def test_update_four_args(self):
        r = Rectangle(4, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", r. __str__())

    def test_update_five_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3,4 , 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", r. __str__())
    
    def test_update_None_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct_output = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct_output, r.__str__())

    def test_update_None_width_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 89)
        correct_output = "[Rectangle] (None) 10/10 - 89/10".format(r.id)
        self.assertEqual(correct_output, r.__str__())

    def test_update_None_width_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 2, 3, 4)
        correct_output = "[Rectangle] (None) 4/10 - 2/3".format(r.id)
        self.assertEqual(correct_output, r.__str__())

    def test_update_nigativeid_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(-89, 2, 3, 4, 5)
        correct_output = "[Rectangle] (-89) 4/5 - 2/3".format(r.id)
        self.assertEqual(correct_output, r.__str__())

    def test_update_morethan_five_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        correct_output = "[Rectangle] (89) 4/5 - 2/3".format(r.id)
        self.assertEqual(correct_output, r.__str__())
    
    def test_update_nigative_x_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 2, 3, -4 , 5)

    def test_update_nigative_y_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 2, 3, 4 , -5)

    def test_update_nigative_width_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0, 3, 4 , -5)
    def test_update__height_ziro_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)
    
    def test_update_width_ziro_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0, 1)
    
    def test_updatenegative_heitgh_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, -3, 4, 5)
    def test_update_x_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"): 
            r.update(89, 1, 2, "invalid", "invalid")

    def test_update_width_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"): 
            r.update(89, 1, "invalid", 2)

    def test_update_height_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"): 
            r.update(89, "invalid",  1,  2)

    def test_update_height_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"): 
            r.update(89, 1,  3,  2, "invalid")

class TestRectangle_update_kwargs(unittest.TestCase):
    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", r. __str__())
    
    def test_update_kwargs_two (self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", r. __str__())
    
    def test_update_kwargs_tree (self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/3", r. __str__())

    def test_update_kwargs_four (self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3, x=4)
        self.assertEqual("[Rectangle] (1) 4/10 - 2/3", r. __str__())

    def test_update_kwargs_five (self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", r. __str__())

    def test_update_kwargs_morethan_five (self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1, width=2, height=3, x=4,y=5, i=10)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", r. __str__())

    def test_update_kwargs_width_nigative_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-2)

    def test_update_kwargs_height_nigative_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-3)
    def test_update_kwargs_x_nigative_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-4)

    def test_update_kwargs_y_nigative_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_kwargs_None(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width=None)
    def test_update_kwargs_width_ziro(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
    def test_update_kwargs_height_ziro(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
    def test_update_kwargs_None(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height=None)
        
    def test_update_kwargs_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")
    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", r. __str__())
class TestRectangle_to_dictionary(unittest.TestCase):
    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct_ouput = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
    def test_to_dictionary_defferent_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        r1 = Rectangle(5, 9, 1, 2, 10)
        correct_ouput = {'x': 9, 'y': 9, 'id': 10, 'height': 5, 'width': 2}
    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()