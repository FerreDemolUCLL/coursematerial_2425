def compact(xs):
    ys = list()
    for item in xs:
        if item != None:
            ys.append(item)
    return ys

def compact_in_place(xs):
    i = 0
    while i < len(xs):
        if xs[i] is None:
            xs.pop(i)
        else:
            i += 1