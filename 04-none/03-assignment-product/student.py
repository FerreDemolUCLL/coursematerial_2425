def product(a, b, c):
    if a == None:
        if b == None:
            if c == None:
                return 1
            else: return c
        elif c == None:
            return b
        else: return b*c
    elif b == None:
        if c == None:
            return a
    
    elif c == None:
        return a*b