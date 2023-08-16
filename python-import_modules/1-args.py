def print_arguments():
    from sys 
    
    num_args = len(argv) - 1
    if num_args == 0:
        args_str = 'arguments:'
    elif num_args == 1:
        args_str = 'argument:'
    else:
        args_str = 'arguments:'
    
    print(num_args, args_str)
    if num_args > 0:
        for i, arg in enumerate(argv[1:], start=1):
            print(i, ":", arg)
            
    print_arguments()
