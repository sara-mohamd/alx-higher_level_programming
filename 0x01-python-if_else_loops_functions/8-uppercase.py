#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
