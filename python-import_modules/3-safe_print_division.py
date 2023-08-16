def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            print("{} / {} = {}".format(a, b, result))
        return result

# Test the function
safe_print_division(10, 2)
