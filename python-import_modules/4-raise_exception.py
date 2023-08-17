def raise_exception():
    value = "Hello, world!"
    if not isinstance(value, int):
        raise TypeError("Expected an integer, but got: " + str(value))

# Call the function to see the exception in action
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)

