def remove_duplicates(xs):
    ys = set()
    result = []
    for item in xs:
        if item not in ys:
            ys.add(item)
            result.append(item)
    return result