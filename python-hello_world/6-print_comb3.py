def main():
    for num in range(10):
        for next_num in range(num + 1, 10):
            print("{:02d}, {:02d}".format(num, next_num), end=", " if next_num < 9 else "\n")

if __name__ == "__main__":
    main()
