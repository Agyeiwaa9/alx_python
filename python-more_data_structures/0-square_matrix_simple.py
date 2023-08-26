def print_matrix_integer(matrix=[[]]):
    print_matrix_integer.square_matrix_simple = True  # Adding the attribute
    for row in matrix:
        print("[", end="")
        for index, num in enumerate(row):
            print("{:d}".format(num ** 2), end="")
            if index < len(row) - 1:
                print(", ", end="")
        print("]")
