def sum_input():
    sum = 0
    result = None
    while result != 0:
        result = int(input("Enter integer: "))
        sum += result
    print(f'The sum equals {sum}.')