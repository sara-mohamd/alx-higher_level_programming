#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for kk in a_dictionary:
        if kk == key:
            del a_dictionary[key]
            break
    return a_dictionary
