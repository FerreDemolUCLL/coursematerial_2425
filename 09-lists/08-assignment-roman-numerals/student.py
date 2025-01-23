def to_roman(n):
    result = ''

    while n >= 1000:
        result += 'M'
        n -= 1000
    if n >= 900:
        result += 'CM'
        n -= 900
    if n >= 500:
        result += 'D'
        n -= 500
    if n >= 400:
        result += 'CD'
        n -= 400
    while n >= 100:
        result += 'C'
        n -= 100
    if n >= 90:
        result += 'XC'
        n -= 90
    if n >= 50:
        result += 'L'
        n -= 50
    if n >= 40:
        result += 'XL'
        n -= 40
    while n >= 10:
        result += 'X'
        n -= 10
    if n >= 9:
        result += 'IX'
        n -= 9
    if n >= 5:
        result += 'V'
        n -= 5
    if n >= 4:
        result += 'IV'
        n -= 4
    while n >= 1:
        result += 'I'
        n -= 1

    return result

def from_roman(string):
    