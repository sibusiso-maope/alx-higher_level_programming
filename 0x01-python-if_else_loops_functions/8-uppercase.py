#!/usr/bin/python3
def to_uper(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return (ord(char) - 32)
    else:
        return ord(char)

def uppercase(string):
    str_new = ""
    for char in string:
        str_new += "%c" % to_uper(char)
    print("{:s}".format(str_new))
