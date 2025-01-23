def gcd(x, y):
    if x < 0:
        x = x*-1
    if y < 0:
        y = y*-1
    if x > y:
        smallest = x
    else: smallest = y
    for i in range(smallest + 1, 0, -1):
        if x % i == 0 and y % i == 0:
            return i