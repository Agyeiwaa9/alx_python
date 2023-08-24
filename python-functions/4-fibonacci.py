def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    
    return fib_list
