 #how to make a key verror handler with built in exception in python

dict = {"name": "Alice", "age": 25}

try:
    print(dict["city"]) 
except KeyError as e:
    print(f"KeyError occurred: {e} - The key does not exist in the dictionary")