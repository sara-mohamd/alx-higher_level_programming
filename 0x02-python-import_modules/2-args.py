#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print(f"{1}: {argv[1]}")
    elif count > 0:
        print(f"{count} arguments:")
        for i in range(1, count + 1):
            print(f"{i}: {argv[i]}")
