#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for elm in my_str:
        if elm != "c" and elm != "C":
            new_str += elm
    return new_str
