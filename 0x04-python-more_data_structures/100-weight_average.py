#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    k = 0
    l = 0

    for m in my_list:
        k += m[0] * m[1]
        l += m[1]

    return (k / l)
