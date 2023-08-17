def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        print(str(e))

# Example usage:
raise_exception_msg("C is fun")
