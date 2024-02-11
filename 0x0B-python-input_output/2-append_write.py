#!/usr/bin/python3
""" Task 2 """


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
     and returns the number of characters added
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
