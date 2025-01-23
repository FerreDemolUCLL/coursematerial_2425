def all_equal(xs):
    j = len(xs)-1
    for i in range(0, j):
        if xs[i] != xs[i+1]:
            return False
        
    return True