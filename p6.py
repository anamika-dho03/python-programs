#Make a attribute error handler with built in exception 
class MyClass:
    def __init__(self):
        self.name = "Alice"

obj = MyClass()

try:
    print(obj.age)  # This will raise an AttributeError
except AttributeError as e:
    print(f"AttributeError occurred: {e} - The attribute does not exist")