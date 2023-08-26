def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is None:
            print("Inside result: None")
        else:
            print("Inside result: {}".format(result))
            print("{} / {} = {}".format(a, b, result))
        return result
