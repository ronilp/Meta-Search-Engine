class struc:
    def __init__(self):
        self.title = ''
        self.description = ''

def find_between(s, first, last):
    start = s.index(first) + len(first)
    end = s.index(last, start)
    return s[start:end]

