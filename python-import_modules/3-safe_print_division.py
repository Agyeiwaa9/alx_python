def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result:", result)
            if b != 0:
                print("{} / {} = {}".format(a, b, result))

# Test the function
safe_print_division(10, 2)
