def increasing(ns):
    for i in range(len(ns)-1):
        j = i+1
        if ns[i] > ns[j]:
            return False
    return True