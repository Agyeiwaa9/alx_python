def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        print("{} / {} = None".format(a, b))
    except Exception as e:
        print("An error occurred:", str(e))
        print("Inside result: None")

    finally:
        if 'result' in locals():
            print("Inside result: {}".format(result))
            if result is not None:
                print("{} / {} = {}".format(a, b, result))
        else:
            print("Inside result: None")
            print("{} / {} = None".format(a, b))
