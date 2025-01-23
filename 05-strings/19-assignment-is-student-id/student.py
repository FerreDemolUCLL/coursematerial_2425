def is_digit(char):
    digits = "0123456789"
    if char in digits:
        return True
    return False

def is_student_id(string):
    nummers = string[1:]
    if string[0].lower() == "r" or string[0].lower() == "s":
        if len(nummers) == 7:
            for nummer in nummers:
                if not is_digit(nummer):
                    return False
            return True
        return False
    return False