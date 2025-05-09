 #Make a index error handler with built in exception 

try:
    print(undeclared_variable)  # This will raise a NameError
except NameError as e:
    print(f"NameError occurred: {e}")