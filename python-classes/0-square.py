class Square:
    def __init__(self, size):
        self.__size = size

# Example usage
square = Square(5)
print(square._Square__size)  # Accessing private attribute (not recommended)

