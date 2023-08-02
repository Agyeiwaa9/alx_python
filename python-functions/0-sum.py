#!/usr/bin/env python3
add = __import__('0-sum').add
def add(a, b):
    # Using bitwise operations to perform addition
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Test the function
result = add(5, 7)
print(result)  # Output will be 12

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))


