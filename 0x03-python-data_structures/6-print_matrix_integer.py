#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for args in range(len(matrix)):
            for element in range(len(matrix[args])):
                if element != len(matrix[args]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[args][element]), end=endspace)
            print()
