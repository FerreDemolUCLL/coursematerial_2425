def pad_right(xs, lenght, padding):
    count = lenght - len(xs)
    
    while count > 0:
        xs.append(padding)
        count -= 1
