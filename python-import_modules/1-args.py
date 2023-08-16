def print_arguments():
    from sys import argv
    
    num_args = len(argv) - 1
    if num_args == 0:
        args_str = '0 arguments.'
    elif num_args == 1:
        args_str = '1 argument:'
    else:
        args_str = f"{num_args} arguments:"
    
    print(args_str)
    for i, arg in enumerate(, start=1):
        print(i, ":", arg)

if __name__ == "__main__":
    print_arguments()

