#!/usr/bin/python3
pow = __import__('1-power').pow

def pow(a, b):
    if b == 0:
        return 1
    result = 1
    abs_b = abs(b)
    while abs_b > 0:
        if abs_b % 2 == 1:
            result *= a
        a *= a
        abs_b //= 2
    return result if b >= 0 else 1 / result

print(pow(-2, 2))
print(pow(2, 2))
print(pow(10, -2))
print(pow(-98, -10))





