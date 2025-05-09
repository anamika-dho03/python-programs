#Make module not found error handler with built in exceptions
try:
    import non_existent_module  # This will raise a ModuleNotFoundError
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError occurred: {e} - The module does not exist")


