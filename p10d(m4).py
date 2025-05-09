import list1
import set2
import dict3

# Example Usage:
lst = [1, 2, 3]
list1.append1(lst, 4)
print(lst)  # [1, 2, 3, 4]
lst2 = [7,9,8]
lst.extend(lst2)
print(lst)
lst.remove(1)
print(lst)

s = {1, 2, 3}
set2.adds2(s, 4)
print(s)  # {1, 2, 3, 4}

d = {"a": 1, "b": 2}
dict3.add3(d, "c", 3)
print(d)  # {'a': 1, 'b': 2, 'c': 3}
