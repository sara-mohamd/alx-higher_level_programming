#!/usr/bin/pyhton3
""" Task 0 """


def read_file(filename=""):
    with open(filename) as file:
        print(file.read(), end="")
