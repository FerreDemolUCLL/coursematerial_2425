def subtuple(xs, ys):
    if len(ys) == 0:
        return True
    
    for i in range(len(xs) - len(ys) + 1):
        if xs[i:i+len(ys)] == ys:
            return True
    return False