def remove_runs(ns):
    if len(ns) == 0:
        return []

    ms = [ns[0]]
    for item in ns[1:]:
        if item != ms[-1]:
            ms.append(item)
    return ms