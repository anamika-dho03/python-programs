 #Make a VALUE error handler with built in exception 
try:
    num = int("abc")  # This will raise a ValueError
except ValueError as e:
    print(f"ValueError occurred: {e} - Invalid value for conversion")