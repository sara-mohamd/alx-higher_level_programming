#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    temp = my_list.copy()
    if my_list is not None and idx >= 0 and idx < len(my_list):
        temp[idx] = element
        return temp
    return my_list
