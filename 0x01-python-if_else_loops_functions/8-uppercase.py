#!/usr/bin/python3
def uppercase(str):
    if len(str) == 0:
        return ""
    result = ""
    if str[0].isalpha():
        if 'a' <= str[0] <= 'z':
            result += chr(ord(str[0]) - 32)
        else:
            result += str[0]
    else:
        result += str[0]
    return result + uppercase(str[1:])
