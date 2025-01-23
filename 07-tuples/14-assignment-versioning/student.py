def increase_version(version, breaking_change, new_features):
    first, second, third = version
    if breaking_change == True:
        first += 1
        second = 0
        third = 0
    
    elif new_features == True:
        second += 1
        third = 0
    
    else:
        third += 1
        
    return (first, second ,third)

def is_more_recent(v1, v2):
    return v1 > v2

def is_older(v1, v2):
    return v1 < v2