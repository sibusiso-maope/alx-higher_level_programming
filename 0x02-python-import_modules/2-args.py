#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLength = len(sys.argv) - 1
    if argLength == 0:
        print("0 arguments.")
    elif argLength == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argLength))
    for k in range(argLength):
        print("{}: {}".format(k + 1, sys.argv[k + 1]))
