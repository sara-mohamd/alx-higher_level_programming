#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not type(roman_string) is str:
        return 0
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and dic[roman_string[i]] < dic[roman_string[i + 1]]:
            sum -= dic[roman_string[i]]
        else:
            sum += dic[roman_string[i]]
    return sum
