def update_dictionary(a_dictionary, key, value):
    # Print dictionary before update
    for k, v in a_dictionary.items():
        print(f"{k}: {v}")
    
    # Update the dictionary
    a_dictionary[key] = value
    
    # Print dictionary after update
    print("xx")
    for k, v in a_dictionary.items():
        print(f"{k}: {v}")

