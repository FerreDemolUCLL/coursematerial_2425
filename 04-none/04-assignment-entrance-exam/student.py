def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    count = 0
    total = 0
    none_count = 0
    grades = [grade1, grade2, grade3, grade4, grade5]
    for grade in grades:
        if grade != None:
            total += grade
            count += 1
        else: none_count += 1
    if none_count > 1: return False
    elif total/count >= 12:
        return True
    else: return False