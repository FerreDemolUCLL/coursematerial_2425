def matching_brackets(string):
    r = 0
    f = 0
    s = 0

    for i in string:
        if i == '(':
            r += 1
        elif i == ')':
            r -= 1
            
        elif i == '{':
            f += 1
        elif i == '}':
            f -= 1
            
        elif i == '[':
            s += 1
        elif i == ']':
            s -= 1

        if r < 0 or f < 0 or s < 0:
            print(False)
            return False
    print(r == 0 and f == 0 and s == 0)
    return r == 0 and f == 0 and s == 0

matching_brackets('([)]')