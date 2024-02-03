#!/usr/bin/python3
""" Q1 """


class MyList(list):
    """ Class inherits from list """


    def __init__(self):
        """ Initializing the instance """
        super().__init__()

    def print_sorted(self):
        """ prints the list, sorted (ASC) """
        print(sorted(self))
