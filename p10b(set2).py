def slen2(s):
    return len(s)

def adds2(s, x):
    s.add(x)

def remove2(s, x):
    s.discard(x)  # `discard()` avoids KeyError if x isn't present
