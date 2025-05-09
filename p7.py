#Make a file not found error handler with built in exceptions

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError occurred: {e} - The file does not exist")