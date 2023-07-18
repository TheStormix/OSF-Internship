class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def calculate_total_price(self):
        total_price = sum(product.price * product.quantity for product in self.products)
        return total_price


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)
        print(f"{product.name} added to {self.name}'s cart.")

    def remove_from_cart(self, product):
        self.cart.remove_product(product)
        print(f"{product.name} removed from {self.name}'s cart.")

    def complete_purchase(self):
        total_price = self.cart.calculate_total_price()
        print(f"{self.name}'s cart total: ${total_price}")


# Test the functionality with the provided cases
product1 = Product("Shirt", 20, 2)
product2 = Product("Shoes", 50, 1)
product3 = Product("Hat", 10, 3)
customer1 = Customer("Alice")
customer2 = Customer("Bob")

customer1.add_to_cart(product1)
customer1.add_to_cart(product2)
customer2.add_to_cart(product3)

customer1.complete_purchase()
customer2.complete_purchase()

customer1.remove_from_cart(product1)
customer1.complete_purchase()
