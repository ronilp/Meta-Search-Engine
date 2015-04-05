class struc:
    def __init__(self):
        self.title = ''
        self.description = ''
        self.url = ''

def find_between(s, first, last):
    start = s.index(first) + len(first)
    end = s.index(last, start)
    return s[start:end]

def intersect(a, b):
     return list(set(a) & set(b))

def union(a, b):
    return list(set(a) | set(b))
