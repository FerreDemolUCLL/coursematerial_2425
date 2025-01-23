def passing_percentage(grades):
    total = 0
    passed = 0
    for grade in grades:
        total += 1
        if grade >= 10:
            passed += 1
    return passed/total*100