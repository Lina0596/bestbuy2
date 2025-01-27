import products
import promotions


class Store:


    def __init__(self, product_list):
        self.products = product_list


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        return f"There are {len(self.products)} items in the store."


    def get_all_products(self):
        active_products = []
        for i in range(len(self.products)):
            if products.Product.is_active(self.products[i]):
                active_products.append(self.products[i])
        return active_products


    def order(self, shopping_list):
        price = 0
        for i in range(len(shopping_list)):
            price += type(shopping_list[i][0]).buy(shopping_list[i][0], shopping_list[i][1])
        return f"${price}"


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    store = Store(product_list)
    all_products = store.get_all_products()
    print(all_products)
    print(store.get_total_quantity())
    print(all_products[0])
    print(store.order([(all_products[3], 6)]))


if __name__ == "__main__":
    main()
