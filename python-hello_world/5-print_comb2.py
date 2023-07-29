def main():
    for num in range(100):
        print("{:02d}".format(num), end=", " if num < 99 else "\n")

if __name__ == "__main__":
    main()
