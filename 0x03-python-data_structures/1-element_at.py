#!/usr/bin/python3


def element_at(my_list, idx):
    # if my_list[idx] < 0:
    #     return
    # elif my_list[idx] < len(my_list):
    #     return
    if idx > 0 and my_list[idx] < len(my_list):
        return my_list[idx]
    else:
        return
