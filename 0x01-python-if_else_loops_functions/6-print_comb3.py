#!/usr/bin/python3
for var in range(0, 9):
    for j in range(0, 10):
        if var == 8 and j == 9:
            print("{}{}".format(var, j), end=(""))
        else:
            print("{}{}, ".format(var, j), end=(""))
