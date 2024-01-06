#!/usr/bin/python3
"""Q5"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "\n":
        print()
        return
    line = ""
    for char in text:
        line += char
        if char in ['.', '?', ':']:
            print(f"{line.strip()} \n")
            line = ""
    print(line.strip(), end=(""))
