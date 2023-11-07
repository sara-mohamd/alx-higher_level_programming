#!/usr/bin/python3


def element_at(my_list, idx):
    if my_list[idx] < 0 or my_list[idx] > (len(my_list) - 1):
        return "None"
    else:
        return my_list[idx]
