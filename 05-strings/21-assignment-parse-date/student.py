def parse_day(string):
    if string[0] == 0:
        return int(string[1])
    return int(string [0:2])

def parse_month(string):
    if string[3] == 0:
        return int(string[4])
    return int(string [3:5])

def parse_year(string):
    return int(string[6:])