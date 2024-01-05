#!/usr/bin/python3
"""
    This function add two numbers:
    a: An integer or float
    b: An integer or float
    return a+B
"""

def add_integer(a, b=98):
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
