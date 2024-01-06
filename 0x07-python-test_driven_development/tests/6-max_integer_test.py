#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test Cases"""
    def test_int(self):
        self.assertEqual(max_integer([10, 5, 6]), 10)
        self.assertEqual(max_integer([4, 8, 15]), 15)
        self.assertEqual(max_integer([4, 10, 8]), 10)
        self.assertEqual(max_integer([-1, -4, -0.5]), -0.5)
        self.assertEqual(max_integer([-1, 1, 0]), 1)
        self.assertEqual(max_integer([3]), 3)
    
    def test_float(self):
        self.assertEqual(max_integer([12, 13.5, 10]), 13.5)
    
    def test_empty(self):
        self.assertEqual(max_integer(), None)
    
    def test_diffDataType(self):
        with self.assertRaises(TypeError):
            max_integer([1, 's', 4])
    
    def test_chars(self):
        self.assertEqual(max_integer(['a', 'h', 'A']), 'h')

