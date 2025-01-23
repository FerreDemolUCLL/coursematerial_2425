def find_duplicates(xs):
    ys = set()
    duplicates = set()
    result = []
    
    for item in xs:
        if item in ys:
            if item not in duplicates:
                result.append(item)
                duplicates.add(item)
        else: ys.add(item)
    return result