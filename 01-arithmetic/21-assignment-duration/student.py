def hours(duration):
    count = 0
    while duration >= 60:
        duration -= 60
        count += 1
    return count