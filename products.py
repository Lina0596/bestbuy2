class Product:


    def __init__(self, name, price, quantity):
        try:
            if name == "":
                raise ValueError("The name is empty.")
            else:
                self.name = name
            if price < 0:
                raise ValueError("The price is negative.")
            else:
                self.price = price
            if quantity < 0:
                raise ValueError("The quantity is negative.")
            else:
                self.quantity = quantity
            self.activate()
        except ValueError as e:
            print(e)


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity >= 1:
            self.deactivate()
        else:
            self.activate()


    def is_active(self):
        if self.quantity > 0:
            return self.activate()
        else:
            return self.deactivate()


    def activate(self):
        active = True
        return active


    def deactivate(self):
        active = False
        return active


    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        try:
            if (self.quantity - quantity) >= 0:
                self.quantity -= quantity
                total_price = float(self.price * quantity)
                return total_price
            elif (self.quantity - quantity) < 0:
                raise ValueError(f"The maximum amount of this product is {self.quantity}!")
        except ValueError as e:
            print(e)


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()