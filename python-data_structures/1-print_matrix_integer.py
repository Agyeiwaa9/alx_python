def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}" .format(num), end="")
            if i < len(row) - 1:
                print()
