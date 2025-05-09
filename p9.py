#Make an error handler with use of multiple except for all typexs errors

try:
    # Sample operations that may cause different errors
    num = int("abc")  # ValueError
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
    my_dict = {"name": "Alice"}
    print(my_dict["age"])  # KeyError
    with open("non_existent_file.txt", "r") as file:  # FileNotFoundError
        content = file.read()
except ValueError as e:
    print(f"ValueError occurred: {e} - Invalid value for conversion")
except IndexError as e:
    print(f"IndexError occurred: {e} - The index is out of range")
except KeyError as e:
    print(f"KeyError occurred: {e} - The key does not exist in the dictionary")
except FileNotFoundError as e:
    print(f"FileNotFoundError occurred: {e} - The file does not exist")
except Exception as e:
    print(f"An unexpected error occurred: {e}")