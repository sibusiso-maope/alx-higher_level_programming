#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    k = 0
    for c in str:
        if k != n:
            new += c
        k += 1
    return new
