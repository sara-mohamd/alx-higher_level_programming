#!/usr/bin/python3
""" Task 1 """


def write_file(filename="", text=""):
    """
    function writes a string to text file
    return number of chars written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
