#!/usr/bin/python3
k = 0
while k <= 89:
    if k % 10 == 0:
        k += 1 + k // 10
    print("{:02d}".format(k), end='\n' if k == 89 else ", ")
    k += 1
