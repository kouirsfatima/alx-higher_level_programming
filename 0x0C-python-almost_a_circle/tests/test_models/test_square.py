#!/usr/bin/python3
"""Defines unittests for base.py.

"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.square import Square
class TestSquare_size(unittest.TestCase):

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_floit_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.2)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2])

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_dic_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3, 2, 3})

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("hello")
    
    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_ziro_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
    def test_invalide_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))
        
class TestSquare_x(unittest.TestCase):

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -3)

    def test_floit_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 2.2)
    
    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, [2])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2, 3))

    def test_dic_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 2, 3, 2, 3})

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "hello")
    
    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)

    def test_invalide_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "invalid")
        
    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, float('nan'))
    
class TestSquare_y(unittest.TestCase):

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_floit_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 2.2)
    
    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 2, [2])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, (1, 2, 3))

    def test_dic_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, {1, 2, 3, 2, 3})

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, "hello")
    
    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, True)

    def test_invalide_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, "invalid")
        
    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, float('nan'))
class TestSquare_position(unittest.TestCase):

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")
class TestSquare_area(unittest.TestCase):

    def test_area(self):
        t = Square(5)
        self.assertNotEqual(t.area(), 50)

    def test_zero(self):
        with self.assertRaises(ValueError, msg="area must be > 0"):
            Square(0, 10)

    def test_one_arg_area(self):
        t = Square(5, 10)
        with self.assertRaises(TypeError):
            t.area(5)
    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_smal_area(self):
        t = Square(5, 2,1)
        self.assertNotEqual(t.area(), 10)

    def test_area(self):
        t = Square(5, 5)
        self.assertNotEqual(t.area(), 10)

    def test_area_long(self):
        t =  Square(100000,2000)
        self.assertNotEqual(t.area(), 200000000)

class TestSquare_desplay(unittest.TestCase):
    def test_dislpay(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Square(2, 0, 2, 12).display()
            self.assertEqual(op.getvalue(), "\n\n##\n##\n")
    
    def test_display_width_height(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Square(2, 3, 0, 0).display()
            self.assertNotEqual("##\n##\n##\n", op.getvalue())

    def test_display_width_height_x(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Square(3, 3, 1, 0).display()
            self.assertNotEqual(" ###\n ###\n", op.getvalue())

    def test_display_width_height_y(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Square(2, 5, 0, 1).display
            self.assertNotEqual("\n####\           ####\n####\n####\n####\n", op.getvalue())

    def test_display_width_height_x_y(self):
        with patch('sys.stdout', new=StringIO()) as op:
            Square(2, 6, 3, 0).display
            self.assertNotEqual( "\n\n   ##\n   ##\n   ##\n   ##\n", op.getvalue())

    def test_display_one_arg(self):
        t = Square(5, 1, 2, 4)
        with self.assertRaises(TypeError):
            t.display(1)
    
class TestSquare_Str(unittest.TestCase):

    def test_str_height_width(self):
        t = Square(5, 1)
        correct_output = "[Square] ({}) 1/0 - 5".format(t.id)
        self.assertEqual(correct_output, t.__str__())

    def test_str_height_width_y(self):
        t = Square(4, 6, 1)
        correct_output = "[Square] ({}) 6/1 - 4".format(t.id)
        self.assertEqual(correct_output, t.__str__())

    def test_str_width_height(self):
            with patch('sys.stdout', new=StringIO()) as op:
                t = Square(4, 6)
                correct_output = "[Square] ({}) 0/0 - 4/6\n".format(t.id)
                self.assertNotEqual(correct_output, op.getvalue().__str__())
    
    def test_str_height_width_x(self):
        t = Square(1, 5, 5)
        correct_output = "[Square] ({}) 5/5 - 1".format(t.id)
        self.assertEqual(correct_output, t.__str__())
    
    def test_str_method_two_arg(self):
        t = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            t.__str__(1/2)

    def test_str_method_zoro(self):
        t = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            t.__str__(0)

    def test_str_method_oneargs(self):
        t = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            t.__str__(1)
    
    def test_str_method_negative(self):
        t = Square (1, 2, 3, 4)
        with self.assertRaises(TypeError):
            t.__str__(-5)

class TestSquare_update_args(unittest.TestCase):

    def test_update_args_ziro_args(self):
        t = Square(10, 10, 10, 10)
        t.update()
        self.assertEqual("[Square] (10) 10/10 - 10", t. __str__())

    def test_update_args_one_args(self):
        t = Square(10, 10, 10, 10)
        t.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", t.__str__())

        def test_update_two_args(self):
            t = Square(10, 10, 10, 10)
        t.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", t.__str__())

    def test_update_tree_args(self):
        t = Square(10, 10, 10, 10)
        t.update(89, 2, 3)
        self.assertNotEqual("[Square] (89) 10/10 - 2/2", t.__str__())

    def test_update_four_args(self):
        t =Square(4, 10, 10, 10)
        t.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", t.__str__())


    def test_update_five_args(self):
        t = Square(10, 10, 10, 10)
        t.update(89, 2, 3,4 , 5)
        self.assertNotEqual("[Square] (89) 3/4- 2/2", t.__str__())
        
    def test_update_nigativeid_args(self):
        t = Square(10, 10, 10, 10)
        t.update(-89, 2, 3, 4, 5)
        correct_output = "[Square] (-89) 3/5 - 2/2".format(t.id)
        self.assertNotEqual(correct_output, t.__str__())

    def test_update_negative_x_args(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                t.update(89, 2, 3, -4)

    def test_update_nigative_x_args(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            t.update(89, 2, -3, 4 , 5)
    

    def test_update_nigative_width_args(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            t.update(89, 0, 3, 4 , -5)

    def test_update_zero_args(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            t.update(89, 0)

    def test_update_args_invalid_x(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            t.update(89, 1, "invalid")

    def test_update_args_size_before_x(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            t.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            t.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            t.update(89, 1, "invalid", "invalid")
            
class TestSquare_update_kwargs(unittest.TestCase):
    def test_update_kwargs_one(self):
        t = Square(10, 10, 10, 10,)
        t.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", t.__str__())
    
    def test_update_kwargs_two (self):
        t = Square(10, 10, 10, 10)
        t.update(id=1, size=2)
        self.assertEqual("[Square] (1) 10/10 - 2", t.__str__())
    
    def test_update_kwargs_tree (self):
        t = Square(10, 10, 10, 10)
        t.update(id=1, size=2, x=3)
        self.assertEqual("[Square] (1) 3/10 - 2", t.__str__())

    def test_update_kwargs_four (self):
        t = Square(10, 10, 10, 10)
        t.update(id=1, size=2, y=3, x=4)
        self.assertEqual("[Square] (1) 4/3 - 2",t.__str__())

    def test_update_kwargs_morethan_five (self):
        t = Square(10, 10, 10, 10)

        t.update(id=1, x=4,y=5, i=10)
        self.assertEqual("[Square] (1) 4/5 - 10", t.__str__())

    def test_update_kwargs_width_nigative_id(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            t.update(size=-2)

    def test_update_kwargs_x_nigative_id(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            t.update(x=-4)

    def test_update_kwargs_y_nigative_id(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            t.update(y=-5)

    def test_update_kwargs_None(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            t.update(size=None)
        
    def test_update_kwargs_invalid_y(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            t.update(y="invalid")

    def test_update_kwargs_x_type(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            t.update(x="invalid")

    def test_update_kwargs_width_type(self):
        t = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            t.update(size="invalid")

    def test_update_kwargs_wrong_keys(self):
        t= Square(10, 10, 10, 10)
        t.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10/10", t.__str__())
    
    def test_update_args_and_kwargs(self):
        t = Square(10, 10, 10, 10)
        t.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", t.__str__())

    def test_update_kwargs_wrong_keys(self):
        t = Square(10, 10, 10, 10)
        t.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", t.__str__())

    def test_update_kwargs_some_wrong_keys(self):
        t = Square(10, 10, 10, 10)
        t.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", t.__str__())

class TestSquare_to_dictionary(unittest.TestCase):
    def test_to_dictionary_output(self):
        t = Square(10, 2, 1, 9)
        correct_ouput = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
    def test_to_dictionary_defferent_output(self):
        t = Square(10, 2, 1, 9)
        t1 = Square(9, 1, 2, 10)
        correct_ouput = {'x': 9, 'y': 9, 'id': 10, 'height': 5, 'width': 2}
    def test_to_dictionary_arg(self):
        t = Square(10, 2, 4, 1)
        with self.assertRaises(TypeError):
            t.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
