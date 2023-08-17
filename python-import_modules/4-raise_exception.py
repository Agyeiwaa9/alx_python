def raise_exception():
    value = "not an integer"
    try:
        result = 10 + value  # This will raise a TypeError
    except TypeError:
        print("Excection has been raised", end='')

