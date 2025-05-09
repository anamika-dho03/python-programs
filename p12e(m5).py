# m5.py
import mypackage.list1 as list1
import mypackage.set2 as set2
import mypackage.dict3 as dict3

# Using list1
lst = []
list1.append1(lst, 10)
list1.extend1(lst, [20, 30])
print("List:", lst)

# Using set2
st = set()
set2.adds2(st, 40)
set2.remove2(st, 40)
print("Set:", st)

# Using dict3
dct = {}
dict3.add3(dct, 'a', 100)
dict3.add3(dct, 'b', 200)
print("Dictionary:", dct)
