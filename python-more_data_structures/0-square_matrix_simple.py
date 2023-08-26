def print_matrix_integer(matrix=[[]], square_matrix_simple=False):
    for row in matrix:
        print("[", end="")
        for index, num in enumerate(row):
            if square_matrix_simple:
                print("{:d}".format(num ** 2), end=", " if index < len(row) - 1 else "")
            else:
                print("{:d}".format(num), end=", " if index < len(row) - 1 else "")
        print("]")
