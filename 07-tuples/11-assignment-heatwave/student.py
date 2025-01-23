def heatwave(temps):
    twentyfive = 0
    thirty = 0
    
    for temp in temps:
        if temp >= 25:
            twentyfive += 1
            if temp >= 30:
                thirty += 1
        else:
            twentyfive = 0
            thirty = 0
    
        if twentyfive >= 5 and thirty >= 3:
            return True
    return False