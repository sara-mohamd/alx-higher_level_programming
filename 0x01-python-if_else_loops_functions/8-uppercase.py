#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if i.isalpha():
            if 'a' <= i <= 'z':
                result += chr(ord(i) - 32)
        else:
            result += i
    print(result)
