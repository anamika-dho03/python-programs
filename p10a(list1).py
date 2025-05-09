def append1(lst, x):
    lst.append(x)

def extend1(lst, l):
    lst.extend(l)

def pop1(lst):
    return lst.pop() if lst else None

def remove1(lst, x):
    if x in lst:
        lst.remove(x)
