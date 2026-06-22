"""
This module contains the Store class which manages a collection of products.
"""

class Store:
    """
    Represents a store that holds products and handles orders.
    """
    def __init__(self, items):
        """
        Initializes the store with a list of products.
        """
        self.items = items

    def add_product(self, product):
        """
        Adds a product to the store.
        """
        if product not in self.items:
            self.items.append(product)
        else: raise ValueError('Product already in store.')

    def remove_product(self, product_to_delete):
        """
        Removes a product from the store.
        """
        if product_to_delete in self.items:
            self.items.remove(product_to_delete)
        else: raise ValueError('This product is not in the database.')

    def get_total_quantity(self):
        """
        Returns the total number of products in the store.
        """
        return sum(item.quantity for item in self.items if item.active == True)

    def get_all_products(self):
        """
        Returns a list of all products in the store.
        """
        return [item for item in self.items if item.active == True]

    def order(self, ordered_items_with_quantity):
        """
        Gets a list of tuples: (Product object, quantity int)
        Buys the products and returns the total price of the order.
        """
        total_order_price = 0.0

        for product_instance, quantity in ordered_items_with_quantity:
            cost_for_this_item = product_instance.buy(quantity)
            total_order_price += cost_for_this_item

        return total_order_price