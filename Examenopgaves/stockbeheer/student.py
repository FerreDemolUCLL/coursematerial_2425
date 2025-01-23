class Part:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._quantity = 0

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError(f"Quantity for part {self.name} can't be negative")
        self._quantity = value

    def info(self):
        return f"{self.name}: Price = {self.price}, Available Quantity = {self.quantity}"


class Stock:
    def __init__(self):
        self._parts = {}

    def add_part(self, name, price, quantity):
        if name in self._parts:
            raise ValueError(f"Part with name {name} already exists in our stock")
        part = Part(name, price)
        part.quantity = quantity
        self._parts[name] = part

    def get_part(self, name):
        return self._parts.get(name)

    @property
    def parts(self):
        return self._parts.values()

    def remove_part(self, name):
        if name in self._parts:
            del self._parts[name]

    def restock_part(self, name, quantity):
        part = self.get_part(name)
        if part:
            part.quantity += quantity


class Shop:
    def __init__(self, name):
        self.name = name
        self._stock = Stock()

    @property
    def stock(self):
        return self._stock

    def load_stock_from_file(self):
        with open('stock.txt', 'r') as file:
            for line in file:
                name, price, quantity = line.strip().split('|')
                self._stock.add_part(name, float(price), int(quantity))

    def save_stock_to_file(self):
        with open('stock.txt', 'w') as file:
            for part in self._stock.parts:
                file.write(f"{part.name}|{part.price}|{part.quantity}\n")

    def display_stock(self):
        stock_info = "Current stock is:\n"
        for part in self._stock.parts:
            stock_info += part.info() + "\n"
        print(stock_info)

    def register_sale(self, name, quantity):
        part = self._stock.get_part(name)
        if not part:
            raise ValueError(f"Part with name {name} does not exist in our stock")
        if part.quantity < quantity:
            raise ValueError(f"Not enough stock for part {name}")
        part.quantity -= quantity
        with open('sales.txt', 'a') as file:
            file.write(f"Sold {quantity} item(s) from product {name} for price {part.price}\n")


def display_menu():
    print("\n===== IT Store Stock Management System =====")
    print("1. Add new part")
    print("2. Restock existing part")
    print("3. Sell part")
    print("4. View stock")
    print("5. Remove existing part")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    shop = Shop("The IT Store")
    shop.load_stock_from_file()

    stop = False
    while not stop:
        choice = display_menu()

        if choice == '1':
            name = input("Enter part name: ")
            price = float(input("Enter part price: "))
            quantity = int(input("Enter part quantity: "))
            shop.stock.add_part(name, price, quantity)

        elif choice == '2':
            name = input("Enter part name: ")
            quantity = int(input("Enter quantity to add: "))
            shop.stock.restock_part(name, quantity)

        elif choice == '3':
            name = input("Enter part name: ")
            quantity = int(input("Enter quantity to sell: "))
            shop.register_sale(name, quantity)

        elif choice == '4':
            shop.display_stock()

        elif choice == '5':
            name = input("Enter part name to remove: ")
            shop.stock.remove_part(name)

        elif choice == '6':
            shop.save_stock_to_file()
            stop = True

        else:
            print("Invalid choice. Please try again.")

main()