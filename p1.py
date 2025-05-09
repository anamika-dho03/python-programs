 #Make a index error handler with built in exception 

def safe_divide(a, b):
    try:

        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    return None


safe_divide(12, 5)
safe_divide(10, 0)