#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    info = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [info[x] for x in roman_string] + [0]
    rep = 0

    for k in range(len(num) - 1):
        if num[k] >= num[k+1]:
            rep += num[k]
        else:
            rep -= num[k]

    return rep
