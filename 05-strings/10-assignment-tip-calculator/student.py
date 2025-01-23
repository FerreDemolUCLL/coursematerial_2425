def tip_calculator():
    price = int(input("Enter total price:"))
    tip = input("Enter tip percentage (default=20):")
    if tip == '':
        pay = price + price*0.2
    else: pay = price + price*int(tip)//100
    print(f"You have to pay {round(pay)}")