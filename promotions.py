from abc import ABC, abstractmethod


class Promotion(ABC):

    def __init__(self, name):
        """
        Creates the instance variables of the Promotion class.
        """
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method to apply a promotion to a product.
        """
        pass


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        """
        Creates the instance variables of the PercentDiscount subclass.
        """
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        """
        Applies the percentage discount to the product
        and returns the discounted price.
        """
        total_price = product.price * quantity
        discount = (total_price / 100) * self.percent
        discounted_price = total_price - discount
        return float(discounted_price)


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        """
        Creates the instance variables of the SecondHalfPrice subclass.
        """
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """
        Checks if the given quantity is valid for discount
        and applies the second half price discount
        (second item at half price) to the product.
        Returns the discounted price.
        """
        total_price = product.price * quantity
        if quantity // 2 >= 1:
            quantity_half_price_products = quantity // 2
            discount = (product.price / 2) * quantity_half_price_products
            discounted_price = total_price - discount
            return float(discounted_price)
        else:
            return float(total_price)


class ThirdOneFree(Promotion):

    def __init__(self, name):
        """
        Creates the instance variables of the ThirdOneFree subclass.
        """
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """
        Checks if the given quantity is valid for discount
        and applies the third one free discount
        (buy 2, get 1 free) to the product.
        Returns the discounted price.
        """
        total_price = product.price * quantity
        if quantity // 3 >= 1:
            quantity_free_products = quantity // 3
            discount = product.price * quantity_free_products
            discounted_price = total_price - discount
            return float(discounted_price)
        else:
            return total_price
