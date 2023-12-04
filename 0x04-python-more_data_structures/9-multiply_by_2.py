#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = a_dictionary.copy()
    for i in temp:
        temp[i] *= 2
    return temp
