#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix in the format
    x x x
    x x x
    x x x
    --
    Args:
        matrix - a matrix of integers default [[]]
    """
    for row in matrix:
        fmt = " ".join(["{:d}" for b in row])
        print(fmt.format(*row))


if __name__ == '__main__':
    mat_trix = [[a, a+1, a+2] for c in range(1, 16, 3)]
    print_matrix_integer(mat_trix)
