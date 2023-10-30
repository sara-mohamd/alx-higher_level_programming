#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1   # as script name is the first element in the script
    sum = 0
    if count == 0:
        print(0)
    elif count > 0:
        for i in range(1, count + 1):
            sum += int(argv[i])
        print(f"{sum}")
