def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
            print("{} / {} = {:.1f}".format(a, b, result))

# Test the function
safe_print_division(10, 2)
