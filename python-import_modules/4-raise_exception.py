def raise_exception():
    value = "not an integer"
    try:
        result = 10 + value  # This will raise a TypeError
    except TypeError:
        print("Exception has been raised", end='')

