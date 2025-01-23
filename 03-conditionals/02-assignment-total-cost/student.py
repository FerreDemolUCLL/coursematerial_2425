def total_cost(amount):
    if amount < 100:
        amount += 10
    if amount >= 200:
        amount = amount - (amount*0.05)
    return amount