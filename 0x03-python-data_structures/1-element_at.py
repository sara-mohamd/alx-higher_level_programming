#!/usr/bin/python3


def element_at(my_list, idx):
    if my_list[idx] < 0 or my_list[idx] > len(my_list):
        return "None"
    else:
        return my_list[idx]
    # if idx > 0 and my_list[idx] < len(my_list):
    #     return my_list[idx]
    # else:
    #     return
