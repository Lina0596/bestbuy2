import promotions

class Product:

    def __init__(self, name, price, quantity):
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
        self.active = True
        self.promotion = None


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def get_promotion(self):
        return self.promotion.name


    def set_promotion(self, promotion):
        self.promotion = promotion


    def show(self):
        if self.promotion is None:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.name}"


    def buy(self, quantity):
        if (self.quantity - quantity) >= 0:
            self.set_quantity(-quantity)
            if self.promotion is None:
                total_price = float(self.price * quantity)
                return total_price
            else:
                total_price = self.promotion.apply_promotion(self, quantity)
                return total_price
        elif (self.quantity - quantity) < 0:
            raise ValueError("Error with your order! Quantity larger than what exists.")


class NonStockedProduct(Product):

    def __init__(self, name, price, quantity=1):
        super().__init__(name, price, quantity)


    def show(self):
        if self.promotion is None:
            return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {self.promotion}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {self.promotion.name}"


    def buy(self, quantity):
        self.quantity += quantity
        return super().buy(quantity)
        

class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        if self.promotion is None:
            return f"{self.name}, Price: ${self.price}, Quantity: Limited to 1 per order!, Promotion: {self.promotion}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: Limited to 1 per order!, Promotion: {self.promotion.name}"


    def buy(self, quantity):
        if quantity == self.maximum:
            return super().buy(quantity)
        elif quantity > self.maximum:
            raise ValueError("Error with your order! Only 1 is allowed from this product.")


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    lic = NonStockedProduct("Windows License", price=125)
    shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)


    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())
    print(lic.buy(3))
    print(shipping.buy(2))

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()