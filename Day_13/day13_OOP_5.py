from abc import ABC, abstractmethod
import math


class Product(ABC):
    def __init__(self, name, price, manufacturer, quantity_in_stock):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.quantity_in_stock = quantity_in_stock

    @abstractmethod
    def get_product_info(self):
        pass

    @abstractmethod
    def set_product_info(self, name, price, manufacturer, quantity_in_stock):
        pass


class Phone(Product):
    def get_product_info(self):
        return f"Phone: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Quantity in stock: {self.quantity_in_stock}"

    def set_product_info(self, name, price, manufacturer, quantity_in_stock):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.quantity_in_stock = quantity_in_stock


class Laptop(Product):
    def get_product_info(self):
        return f"Laptop: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Quantity in stock: {self.quantity_in_stock}"

    def set_product_info(self, name, price, manufacturer, quantity_in_stock):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.quantity_in_stock = quantity_in_stock


class TV(Product):
    def get_product_info(self):
        return f"TV: {self.name}, Price: {self.price}, Manufacturer: {self.manufacturer}, Quantity in stock: {self.quantity_in_stock}"

    def set_product_info(self, name, price, manufacturer, quantity_in_stock):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.quantity_in_stock = quantity_in_stock


class Order:
    def __init__(self, customer_name, customer_address):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.products = []
        self.total_amount = 0

    def add_product(self, product):
        self.products.append(product)
        self.total_amount += product.price

    def calculate_total_amount(self):
        return self.total_amount

    def show_order_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer Address: {self.customer_address}")
        print("Products in the order:")
        for product in self.products:
            print(product.get_product_info())
        print(f"Total Amount: {self.total_amount}")


# Example usage:
# Create product instances
phone = Phone("iPhone 13", 999, "Apple", 50)
laptop = Laptop("MacBook Pro", 1999, "Apple", 30)
tv = TV("Samsung QLED", 1500, "Samsung", 20)

# Create an order
order = Order("John Doe", "123 Main St")

# Add products to the order
order.add_product(phone)
order.add_product(laptop)
order.add_product(tv)

# Show order details
order.show_order_details()
