#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        x = []
        for i in my_list:
           x.append(i % 2 == 0)
        return x
    else:
        return "None"

        