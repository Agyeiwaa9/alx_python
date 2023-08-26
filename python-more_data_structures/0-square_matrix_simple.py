def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print("[", end="")
        for i, num in enumerate(row):
            print("{:d}".format(num ** 2), end="")
            if i < len(row) - 1:
                print(", ", end="")
        print("]")
