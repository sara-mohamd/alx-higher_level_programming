#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in map(lambda pair: f"{pair[0]} : {pair[1]}", sorted(a_dictionary.items())):
        print(i)
