import promotions

class Product:

    def __init__(self, name, price, quantity):
        """
        Creates the instance variables of the Product class (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.
        """
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
        """
        Gets the quantity of the product and returns it.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Sets the quantity based on the given quantity parameter.
        If quantity reaches 0, deactivates the product
        """
        self.quantity += quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """
        Checks if a product is active or not.
        Returns True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activates a product (sets the active status to True).
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates a product (sets the active status to False).
        """
        self.active = False


    def get_promotion(self):
        """
        Gets the promotion of a product and returns it.
        Returns None if there is no promotion.
        """
        return self.promotion.name


    def set_promotion(self, promotion):
        """
        Sets the promotion.
        """
        self.promotion = promotion


    def show(self):
        """
        Returns a string that represents the product.
        """
        if self.promotion is None:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {self.promotion.name}"


    def buy(self, quantity):
        """
        Updates the quantity and buys the given quantity of the product.
        Returns the total price of the purchase.
        Raises exception, if the quantity is larger than what exists.
        """
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
        """
        Creates the instance variables of the NonStockedProduct subclass.
        This class is for products, which are not physical and the quantity
        doesn't have to be tracked.
        """
        super().__init__(name, price, quantity)


    def show(self):
        """
        Returns a string that represents the product.
        """
        if self.promotion is None:
            return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {self.promotion}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {self.promotion.name}"


    def buy(self, quantity):
        """
        Updates the quantity and buys the given quantity of the product.
        Returns the total price of the purchase.
        Raises exception, if the quantity is larger than what exists.
        """
        self.quantity += quantity
        return super().buy(quantity)
        

class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum=1):
        """
        Creates the instance variables of the LimitedProduct subclass.
        This class is for products, which have a limited quantity of 1 per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        """
        Returns a string that represents the product.
        """
        if self.promotion is None:
            return f"{self.name}, Price: ${self.price}, Quantity: Limited to 1 per order!, Promotion: {self.promotion}"
        else:
            return f"{self.name}, Price: ${self.price}, Quantity: Limited to 1 per order!, Promotion: {self.promotion.name}"


    def buy(self, quantity):
        """
        Updates the quantity and buys the given quantity of the product.
        Returns the total price of the purchase.
        Raises exception, if the quantity is larger than what exists.
        """
        return super().buy(quantity)


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