def all_different(xs):
    for i in range(len(xs)-1):
        for j in range(1, len(xs)):
            if i != j:
                if xs[i] == xs[j]:
                    return False
    return True