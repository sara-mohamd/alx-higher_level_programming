#!/usr/bin/python3


def no_c(my_string):
    if my_string is not None:
        result = ''
        for i in my_string:
            if i.upper() != 'C':
                result += i
        return result

            