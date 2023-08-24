#!/usr/bin/env python3

def add(a, b):
    # Using bitwise operations to perform addition
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a






