#!/usr/bin/python3

def add(a, b):
    """My addition function
    Args:
        a: First operand
        b: Second operand
    Returns:
        The sum of a and b
    """
    return a + b

def subtract(a, b):
    """My subtraction function
    Args:
        a: First operand
        b: Second operand
    Returns:
        The difference between a and b
    """
    return a - b

a = 1
b = 2

from add_0 import add

result = add(a, b)
result2 = subtract(a, b)

print("{} + {} = {}\n{} - {} = {}\n".format(a, b, result, a, b, result2))

if __name__ == "__main__":
    pass  # Add your main code here if needed
