def invest(amount, rate, goal):
    time = 0
    while amount < goal:
        time += 1
        amount = amount + amount*rate/100
    return time