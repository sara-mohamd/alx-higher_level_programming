#!/usr/bin/python3
import hidden_4


def discovr():
    name = dir(hidden_4)
    for x in name:
        if x[:2] != '__':
            print("{:s}".format(x))


if __name__ == "__main__":
    discovr()