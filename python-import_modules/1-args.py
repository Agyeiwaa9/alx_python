def print_arguments():
    from sys import argv
    
    num_args = len(argv) - 1
    if num_args == 0:
        args_str = '.'
    elif num_args == 1:
        args_str = 'argument:'
    else:
        args_str = 'arguments:'
    
    print("Number of argument(s) followed by", args_str)
    if num_args > 0:
        for i, arg in enumerate(argv[1:], start=1):
            print(i, ":", arg)

if __name__ == "__main__":
    print_arguments()

