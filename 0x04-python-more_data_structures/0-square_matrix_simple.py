#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    result = []
    for i in range(len(matrix)):
        squared = list(map(lambda a: a**2, matrix[i]))
        result.append(squared)
    return result
