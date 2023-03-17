#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Square all entries of a matrix

    @Arg:
        the matrix
        """
    if not matrix:
                print()
    return [[i**2 for i in row] for row in matrix]
