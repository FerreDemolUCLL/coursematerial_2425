def valid_parentheses(string):
    count = 0

    for i in string:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0:
            return False
    
    if count != 0:
        return False
    return True