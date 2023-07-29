#!/usr/bin/python3
import random

def main():
    number = random.randint(-100, 100)
# YOUR CODE HERE
    print(number)

    if number > 0:
        print("is positive")
    elif number == 0:
        print("is zero")
    else:
        print("is negative")

if __name__ == "__main__":
    main()

