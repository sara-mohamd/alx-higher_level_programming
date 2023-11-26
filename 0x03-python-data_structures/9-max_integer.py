#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        x = my_list[0]
        for i in my_list:
            if i > x:
                x = i
        return x
    return "None"
