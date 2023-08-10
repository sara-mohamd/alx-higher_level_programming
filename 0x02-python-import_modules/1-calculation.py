#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import Addition, Subtructoin, Multiplication, Divsion

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, Addition(a, b)))
    print("{} - {} = {}".format(a, b, Subtructoin(a, b)))
    print("{} * {} = {}".format(a, b, Multiplication(a, b)))
    print("{} / {} = {}".format(a, b, Divsion(a, b)))