def box(string):
    top = "+" + "-"*(len(string)+2) + "+\n"
    middle = "| " + string + " |\n"
    bottom = "+" + "-"*(len(string)+2) + "+"
    return top + middle + bottom