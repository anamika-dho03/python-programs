#how to make a index error handler with built in exception in python

list = [1, 2, 3]

try:
    print(list[5])  
except IndexError as e:
    print(f"IndexError occurred: {e} - The index is out of range")