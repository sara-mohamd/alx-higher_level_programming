#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in map(lambda p: f"{p[0]} : {p[1]}", sorted(a_dictionary.items())):
        print(i)
