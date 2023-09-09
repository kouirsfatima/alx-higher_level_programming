#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for a in range(len(matrix[i])):
            if a == 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][a]), end=" ")
        print()