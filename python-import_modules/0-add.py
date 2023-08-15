#!/usr/bin/python3
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

a = 1
b = 2

from add_0 import add

result = add(a, b)
result2 = subtract(a, b)
print("{} - {} = {}\n".format(a, b, result2))

if __name__ == "__main__":
   pass  # Add your main code here if needed
