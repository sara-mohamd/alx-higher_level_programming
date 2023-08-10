#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import system

    count = len(system.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, system.argv[i + 1]))