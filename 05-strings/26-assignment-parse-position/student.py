def parse_position_x(string):
    string = string[1,-1]
    s = string.find(",")
    x = int(string[:s])
    return x
    

def parse_position_y(string):
    string = string[1,-1]
    s = string.find(",")
    y = int(string[s+1:])
    return y