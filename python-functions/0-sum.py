def add(a, b):
    while b != 0:
        carry = a & b
        a = (a ^ b) & 0xFFFFFFFF
        b = (carry << 1) & 0xFFFFFFFF
    return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)
