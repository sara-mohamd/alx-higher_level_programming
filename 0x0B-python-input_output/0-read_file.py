#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """
    Function that reads a text file and print its content
    """
    with open(filename, "r", encoding='utf-8') as file:
        print(file.read(), end="")
