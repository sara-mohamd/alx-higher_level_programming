#!/usr/bin/python3


def add_integer(a, b=98):
    if not isinstance(a, (float, int)):
        return "a must be an integer"
    elif not isinstance(b, (float, int)):
        return"b must be an integer"
    else:
        return int(a) + int(b)
